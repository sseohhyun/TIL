from django.urls import path
from . import views

urlpatterns = [
    path('<int:genre_id>/', views.genre_detail),
]