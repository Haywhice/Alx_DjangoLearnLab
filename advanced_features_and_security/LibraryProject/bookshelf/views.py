from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators

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
    
@method_decorator(permission_required())