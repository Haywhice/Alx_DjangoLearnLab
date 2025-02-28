from django.shortcuts import render, redirect
from .models import Book
from django.views.generic import DetailView
from .models import Library
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.views.generic.detail import DetailView
# Create your views here.
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html',{'books':books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
    
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account created for {username}")
            return redirect("login")
        else:
            form = UserCreationForm()
        return render(request, "register.html", {"form": form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get['username']
        password = request.POST.get['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password")
    return render(request, "login.html")

def user_logout(request):
    logout(request)
    messages.succes(request, "You have been logged out.")
    return redirect("login")