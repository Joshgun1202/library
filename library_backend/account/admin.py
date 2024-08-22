from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'phone_number',)
    search_fields = ('username', 'phone_number',)

admin.site.register(User, UserAdmin)
