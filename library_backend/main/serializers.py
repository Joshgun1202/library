from rest_framework import serializers
from .models import (
    Book,
    Author,
    Genre,
    Favourite,
)


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'biography', 'created_at_formatted',)

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'name', 'created_at_formatted',)

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Book
        fields = (
            'id',
            'title',
            'author',
            'description',
            'price',
            'get_book',
            'get_book_ext',
            'get_book_size',
            'get_image',
            'genre',
            'published_at',
            'created_at',
            'rating_count',
            'favourites_count',
        )

class FavouriteSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)

    class Meta:
        model = Favourite
        fields = ('id', 'user', 'book', 'created_at_formatted',)