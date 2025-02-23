from django.db import models

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
                return self.name
           
