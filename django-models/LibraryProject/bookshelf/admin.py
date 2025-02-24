from django.contrib import admin
from .models import Book

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year", "cover")
    search_fields = ("title", "author", "publication_year", "cover")
    
admin.site.register(Book, BookAdmin)