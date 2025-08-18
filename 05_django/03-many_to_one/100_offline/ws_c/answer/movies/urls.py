from django.urls import path
from . import views

urlpatterns = [
    path("", views.movie_list),
    path("<int:director_id>/", views.movie_create),


]