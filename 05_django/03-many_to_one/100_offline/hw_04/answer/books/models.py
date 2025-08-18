from django.db import models
from authors.models import Author

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=200)


    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre, related_name='books')

    def __str__(self):
        return self.title


