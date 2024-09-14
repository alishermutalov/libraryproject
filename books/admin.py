from django.contrib import admin
from .models import Book, Author
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    
class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('first_name',)}

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)