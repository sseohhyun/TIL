
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_list_or_404, get_object_or_404
from .serializers import MovieSerializer
from .models import Movie
from directors.models import Director



# Create your views here.
@api_view(["GET"])
def movie_list(request):
    movies = get_list_or_404(Movie)
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(["POST"])
def movie_create(request, director_id):
    director = get_object_or_404(Director, pk=director_id)
    serializer = MovieSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(director=director)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
