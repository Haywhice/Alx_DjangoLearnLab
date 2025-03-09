from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .models import Book
from .forms import BookForm
from .forms import BookSearchForm 
from .forms import ExampleForm 
from django.views.decorators.csrf import csrf_protect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required

# Create your views here.
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"
    
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
    
@user_passes_test(lambda u: u.userprofile.role == 'Admin')
class AdminView(TemplateView):
    template_name = "relationship_app/admin_view.html"
    

@user_passes_test(lambda u: u.userprofile.role == 'Librarian')
class LibrarianView(TemplateView):
    template_name = "relationship_app/Librarian_view.html"

@user_passes_test(lambda u: u.userprofile.role == 'Member')
class MemberView(TemplateView):
    template_name = "relationship_app/Member_view.html"
    
@permission_required('bookshelf.can_edit_book', raise_exception=True)
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'bookshelf/book_form.html', {'form': form})
