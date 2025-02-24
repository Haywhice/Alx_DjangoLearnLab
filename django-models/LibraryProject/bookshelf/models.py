from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    cover = models.CharField(max_length=100, default="Hard cover")
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
