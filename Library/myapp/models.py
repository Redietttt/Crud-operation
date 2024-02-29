
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField()

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)  
    isbn = models.CharField(max_length=20)
    genre = models.CharField(max_length=50)

    def __str__(self):
        return self.title