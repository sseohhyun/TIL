
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .serializers import DirectorSerializer
from .models import Director

# Create your views here.
@api_view(["GET", "POST"])
def director_list_create(request):
    if request.method == "GET":
        directors = Director.objects.all()
        serializer = DirectorSerializer(directors, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = DirectorSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET", "PUT", "DELETE"])
def director_fetch_update_delete(request, pk):
    director = get_object_or_404(Director, pk=pk)

    if request.method == "GET":
        serializer = DirectorSerializer(director)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = DirectorSerializer(director, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method == "DELETE":
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
