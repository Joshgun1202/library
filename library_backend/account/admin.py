from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'firstname', 'lastname')
    search_fields = ('username', 'firstname', 'lastname')

admin.site.register(User, UserAdmin)
