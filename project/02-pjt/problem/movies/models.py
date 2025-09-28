from django.db import models

class Genre(models.Model):
    # movies_genre
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Movie(models.Model):
    # movies_movie
    id = models.IntegerField(primary_key=True)         # CSV의 id 사용
    title = models.CharField(max_length=255)
    release_date = models.DateField(null=True, blank=True)
    popularity = models.FloatField(null=True, blank=True)
    budget = models.IntegerField(null=True, blank=True)
    revenue = models.IntegerField(null=True, blank=True)
    runtime = models.IntegerField(null=True, blank=True)

    # movies_movie_genres (중간 테이블 자동 생성: movies_movie_genres)
    genres = models.ManyToManyField(Genre, related_name='movies', blank=True)

    def __str__(self):
        return self.title

class Cast(models.Model):
    # movies_cast
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='casts')
    name = models.CharField(max_length=255)
    character = models.CharField(max_length=255, null=True, blank=True)
    order = models.IntegerField(null=True, blank=True)

class Review(models.Model):
    # movies_review
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    author = models.CharField(max_length=255)
    content = models.TextField()
    rating = models.FloatField(null=True, blank=True)