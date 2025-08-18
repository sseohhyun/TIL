from django.db import models
from directors.models import Director

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=255)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} ({self.director})'
