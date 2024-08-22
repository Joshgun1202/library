from django.contrib import admin
from .models import Book, Author, Purchase, Review, Favourite, Genre


class BookAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('id', 'title', 'author', 'published_at', 'price', 'pages', 'get_book_ext', 'get_book_size', 'get_book', 'get_image', 'genre', 'description', 'created_at_formatted', 'rating_count', 'favourites_count',)
    search_fields = ('title', 'author', 'description', 'price',)

admin.site.register(Book, BookAdmin)


class AuthorAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('id', 'name', 'biography', 'created_at_formatted',)
    search_fields = ('name', 'biography',)

admin.site.register(Author, AuthorAdmin)


class PurchaseAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('id', 'user', 'book', 'price', 'created_at_formatted',)
    search_fields = ('user', 'book', 'price',)

admin.site.register(Purchase, PurchaseAdmin)


class ReviewAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('id', 'user', 'book', 'rating', 'created_at_formatted',)
    search_fields = ('user', 'book', 'rating',)

admin.site.register(Review, ReviewAdmin)


class FavouriteAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('id', 'user', 'book', 'created_at_formatted',)
    search_fields = ('user', 'book',)

admin.site.register(Favourite, FavouriteAdmin)


class GenreAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('id', 'name', 'created_at_formatted',)
    search_fields = ('name',)

admin.site.register(Genre, GenreAdmin)


