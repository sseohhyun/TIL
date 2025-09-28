from django.contrib import admin
from .models import Movie, Genre, Cast, Review

admin.site.register([Movie, Genre, Cast, Review])
