from rest_framework import serializers
from directors.serializers import DirectorSerializer
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    director = DirectorSerializer(read_only=True)
    class Meta:
        model = Movie
        fields = '__all__'


