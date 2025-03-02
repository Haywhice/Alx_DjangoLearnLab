from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Author Model
class Author(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
#Book model
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    
    class Meta:
        permissions = [
            ("can_add_book", "Can add a book"),
            ("can_change_book", "Can edit a book"),
            ("can_delete_book", "Can delete a book"),
        ]
        
    def __str__(self):
        return self.title
    
    #Library Model
class Library(models.Model):
    name = models.CharField(max_length=255)
    books = models.ManyToManyField(Book)
        
    def __str__(self):
        return self.name
        
#Librarian Model
class Librarian(models.Model):
    name = models.CharField(max_length=255)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)
            
    def __str__(self):
        return self.names

class UserProfile(models.Model):
    ROLE_CHOICE = [
        ("Admin", "Admin"),
        ("Librarian", "Librarian"),
        ("Member", "Member"),
    ]
    user = models.OneToOneField(user, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICE)

    def __str__(self):
        return