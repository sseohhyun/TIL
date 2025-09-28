from django.urls import path
from . import views

urlpatterns = [
    path("genres/", views.genre_list),
    path("movies/", views.movie_list),
    path("movies/<int:movie_pk>/", views.movie_detail),
    path("reviews/", views.review_list),
    path("reviews/<int:review_pk>/", views.review_detail),
    path("movie/<int:movie_pk>/review/", views.create_review_for_movie),
]