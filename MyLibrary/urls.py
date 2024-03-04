from django.urls import path
from . import views

urlpatterns = [
    path("hello", views.hello_world, name="hello"),
    path("books", views.add_book, name="add_book"),
    path("books/<int:id>", views.delete_book, name="delete_book"),  
    path("users", views.insert_user, name="insert_user"),
    path("borrow_book/<int:book_id>/<int:user_id>", views.borrow_book, name="borrow_book"),
]

