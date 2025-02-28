from django.urls import path
from . import views
from .views import list_books, LibraryDetailView
from .views import add_book, edit_book, delete_book

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('books/', list_books, name='list_books'),  # Function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # Class-based view
    path('add/', add_book, name='add_book'),
    path('edit/<int:book_id>/', edit_book, name='edit_book'),
    path('delete/<int:book_id>/', delete_book, name='delete_book'),
]