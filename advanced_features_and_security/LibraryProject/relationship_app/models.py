from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

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
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
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
        return f"{self.user.username} - {self.role}"
    
class CustomUserManager(BaseUserManager):
    """Manager for CustomUser model"""

    def create_user(self, username, email, password=None, **extra_fields):
        """Create and return a regular user"""
        if not email:
            raise ValueError("Email field is required")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)  # Encrypts password
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        """Create and return a superuser"""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(username, email, password, **extra_fields)

class CustomUser(AbstractUser):
    """Custom user model that extends Django’s default User"""
    email = models.EmailField(unique=True)  # Make email required
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to="profile_photos/", null=True, blank=True)

    objects = CustomUserManager()  # Assign our custom manager

    def __str__(self):
        return self.username
    