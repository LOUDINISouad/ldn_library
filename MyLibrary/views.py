from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from datetime import datetime
from .models import Book, User
from .serializers import BookSerializer, UserSerializer

@csrf_exempt
def add_book(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        book_serializer = BookSerializer(data=data)
        if book_serializer.is_valid():
            book_serializer.save()
            return JsonResponse(book_serializer.data, status=201)
        return JsonResponse(book_serializer.errors, status=400)

    elif request.method == "GET":
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def delete_book(request, id):
    try:
        book = Book.objects.get(id=id)
    except Book.DoesNotExist:
        return JsonResponse({'message': 'Book not found'}, status=404)

    if request.method == "DELETE":
        book.delete()
        return JsonResponse({'success': True})

@csrf_exempt
def insert_user(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data, status=201)
        return JsonResponse(user_serializer.errors, status=400)

    elif request.method == "GET":
        users = User.objects.all()
        user_serializer = UserSerializer(users, many=True)
        return JsonResponse(user_serializer.data, safe=False)

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

def hello_world(request):
    return HttpResponse("Hello World")
