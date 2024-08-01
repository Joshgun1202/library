from .serializers import (
    BookSerializer,
    AuthorSerializer,
    GenreSerializer,
    FavouriteSerializer,
)
from .models import (
    Book,
    Author,
    Genre,
    Favourite,
)
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404


class MyCustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000

@api_view(['GET'])
def book_list(request):
    books = Book.objects.all()
    paginator = MyCustomPagination()
    paginated_books = paginator.paginate_queryset(books, request)
    serializer = BookSerializer(paginated_books, many=True)

    return paginator.get_paginated_response(serializer.data)

@api_view(['GET'])
def book_detail(request, pk):
    try:
        book = Book.objects.get(pk=pk)
        serializer = BookSerializer(book)

        return JsonResponse(serializer.data)
    except Book.DoesNotExist:
        return JsonResponse({'error': 'Book does not exist'}, status=404)

@api_view(['GET'])
def books_by_author(request, pk):
    try:
        author = Author.objects.get(pk=pk)
        books = Book.objects.filter(author=author)
        paginator = MyCustomPagination()
        paginated_books = paginator.paginate_queryset(books, request)
        serializer = BookSerializer(paginated_books, many=True)

        return paginator.get_paginated_response(serializer.data)
    except Author.DoesNotExist:
        return JsonResponse({'error': 'Author does not exist'}, status=404)

@api_view(['GET'])        
def books_by_genre(request, pk):
    try:
        genre = Genre.objects.get(pk=pk)
        books = Book.objects.filter(genre=genre)
        paginator = MyCustomPagination()
        paginated_books = paginator.paginate_queryset(books, request)
        serializer = BookSerializer(paginated_books, many=True)

        return paginator.get_paginated_response(serializer.data)
    except Genre.DoesNotExist:
        return JsonResponse({'error': 'Genre does not exist'}, status=404)

@api_view(['POST'])
def like_book(request, pk):
    user = request.user
    book = get_object_or_404(Book, pk=pk)

    try:
        favourite = Favourite.objects.get(user=user, book=book)
        favourite.delete()

        return JsonResponse({'message': 'Book unliked'}, status=200)
    except Favourite.DoesNotExist:
        Favourite.objects.create(user=user, book=book)

        return JsonResponse({'message': 'Book liked'}, status=200)

@api_view(['GET'])
def user_favourite_books(request):
    user = request.user
    favourites = Favourite.objects.filter(user=user)
    paginator = MyCustomPagination()
    paginated_favourites = paginator.paginate_queryset(favourites, request)
    serializer = FavouriteSerializer(paginated_favourites, many=True)

    return paginator.get_paginated_response(serializer.data)

@api_view(['GET'])
def author_list(request):
    authors = Author.objects.all()
    paginator = MyCustomPagination()
    paginated_authors = paginator.paginate_queryset(authors, request)
    serializer = AuthorSerializer(paginated_authors, many=True)

    return paginator.get_paginated_response(serializer.data)

@api_view(['GET'])
def author_detail(request, pk):
    try:
        author = Author.objects.get(pk=pk)
        serializer = AuthorSerializer(author)

        return JsonResponse(serializer.data)
    except Author.DoesNotExist:
        return JsonResponse({'error': 'Author does not exist'}, status=404)

@api_view(['GET'])
def genre_list(request):
    genres = Genre.objects.all()
    serializer = GenreSerializer(genres, many=True)

    return JsonResponse(serializer.data, safe=False)
