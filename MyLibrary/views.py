from http.client import HTTPException
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from MyLibrary.models import Book
from MyLibrary.serializers import BookSerializer
from datetime import datetime
from django.http import JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from .models import Book, User
from .serializers import BookSerializer, UserSerializer

def hello_world(request):
    return HttpResponse("Hello World")

@csrf_exempt
def add_book(request):
   
    if request.method == "POST":
        data = JSONParser().parse(request)

        book_serializer = BookSerializer(data=data)
        if book_serializer.is_valid():
            book_serializer.save()
        else:
            return HTTPException()
        
        return JsonResponse(book_serializer.data)
    
    # get all books
    if request.method == "GET":
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return JsonResponse(serializer.data, safe=False)
    
@csrf_exempt
def delete(request, id):
    if request.method == "DELETE":
        book = Book(id=id)
        book.delete()

# 1. Vue pour obtenir un seul livre par son ID
@csrf_exempt
def get_book_by_id(request, id):
    if request.method == "GET":
        try:
            book = Book.objects.get(id=id)
            serializer = BookSerializer(book)
            return JsonResponse(serializer.data)
        except Book.DoesNotExist:
            return JsonResponse({'message': 'Book not found'}, status=404)

# 2. Modifier le modèle de Livre et Créer une nouvelle vue pour emprunter un livre
@csrf_exempt
def borrow_book(request, book_id, user_id):
    try:
        book = Book.objects.get(id=book_id)
        user = User.objects.get(id=user_id)
    except (Book.DoesNotExist, User.DoesNotExist):
        return JsonResponse({'message': 'Book or user not found'}, status=404)
    
    if request.method == 'POST':
        if book.is_borrowed:
            return JsonResponse({'message': 'Book already borrowed'}, status=400)
        
        book.is_borrowed = True
        book.borrower = user
        book.borrowed_date = datetime.now()
        book.save()

        book_serializer = BookSerializer(book)
        user_serializer = UserSerializer(user)

        return JsonResponse({
            'message': f'Book "{book.title}" is now borrowed by {user.first_name} {user.last_name} on {book.borrowed_date}',
            'book': book_serializer.data,
            'borrower': user_serializer.data,
        })

    return JsonResponse({'message': 'Invalid request method'}, status=400)

# 3. Enregistrer la date d'emprunt lorsque le livre est emprunté
# Cela est déjà pris en charge dans la vue borrow_book

# 4. Rajouter des règles de vérification
@csrf_exempt
def Insert_book(request):
    if request.method == "POST":
        data = JSONParser().parse(request)

        book_serializer = BookSerializer(data=data)
        if book_serializer.is_valid():
            title = data.get('title')
            author = data.get('author')
            if Book.objects.filter(title=title, author=author).exists():
                raise Http404("Ce livre est déjà présent dans la base de données.")

            book_serializer.save()
            return JsonResponse(book_serializer.data)
        else:
            return JsonResponse({'message': 'Invalid data'}, status=400)

    if request.method == "GET":
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return JsonResponse(serializer.data, safe=False)
        
        