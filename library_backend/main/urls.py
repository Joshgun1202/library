from . import api
from django.urls import path


urlpatterns = [
    path('books/', api.book_list, name='book_list'),
    path('books/<int:pk>/', api.book_detail, name='book_detail'),
    path('books/by-author/<int:pk>/', api.books_by_author, name='books_by_author'),
    path('books/by-genre/<int:pk>/', api.books_by_genre, name='books_by_genre'),
    path('books/<int:pk>/like/', api.like_book, name='like_book'),
    path('books/favourites/', api.user_favourite_books, name='user_favourite_books'),

    path('authors/', api.author_list, name='author_list'),
    path('authors/<int:pk>/', api.author_detail, name='author_detail'),

    path('genres/', api.genre_list, name='genre_list'),
]