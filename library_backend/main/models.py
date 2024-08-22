from django.db import models
from account.models import User
from django.conf import settings
from django.utils.timesince import timesince


class Author(models.Model):
    name = models.CharField(max_length=255)
    biography = models.TextField(default='Empty')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)

    def created_at_formatted(self):
        return timesince(self.created_at)
    
    def updated_at_formatted(self):
        return timesince(self.updated_at)

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'


class Genre(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)

    def created_at_formatted(self):
        return timesince(self.created_at)
    
    def updated_at_formatted(self):
        return timesince(self.updated_at)

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Author')
    description = models.TextField(default='...')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    book = models.FileField(upload_to='books', max_length=500)
    pages = models.IntegerField(default=0)
    image = models.ImageField(upload_to='books_images', max_length=500)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, verbose_name='Genre')
    published_at = models.CharField(max_length=4, default='....')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    rating_count = models.IntegerField(default=0)
    favourites_count = models.IntegerField(default=0)

    def __str__(self):
        return str(self.title)

    def get_book(self):
        if self.book:
            return settings.WEBSITE_URL + self.book.url
        else:
            return ''

    def get_book_ext(self):
        ext = self.book.name.split('.')[-1]
        return f".{ext}"

    def get_book_size(self):
        size_in_mb = self.book.size / (1024 * 1024)
        return "{:.2f} Mb".format(size_in_mb)

    def get_image(self):
        if self.image:
            return settings.WEBSITE_URL + self.image.url
        else:
            return ''

    def created_at_formatted(self):
        return timesince(self.created_at)
    
    def updated_at_formatted(self):
        return timesince(self.updated_at)

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'


class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='Book')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.purchased_at)

    def created_at_formatted(self):
        return timesince(self.created_at)
    
    def updated_at_formatted(self):
        return timesince(self.updated_at)

    class Meta:
        verbose_name = 'Purchase'
        verbose_name_plural = 'Purchases'


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='Book')
    rating = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.created_at)

    def created_at_formatted(self):
        return timesince(self.created_at)
    
    def updated_at_formatted(self):
        return timesince(self.updated_at)

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'


class Favourite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='Book')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.created_at)

    def created_at_formatted(self):
        return timesince(self.created_at)
    
    def updated_at_formatted(self):
        return timesince(self.updated_at)

    class Meta:
        verbose_name = 'Favourite'
        verbose_name_plural = 'Favourites'


