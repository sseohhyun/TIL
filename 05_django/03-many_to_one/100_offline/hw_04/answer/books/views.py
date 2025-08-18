
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Genre
from .serializers import GenreSerializer

# Create your views here.
@api_view(['GET'])
def genre_detail(request, genre_id):
    genre = get_object_or_404(Genre, pk=genre_id)
    serializer = GenreSerializer(genre)
    return Response(serializer.data)