from rest_framework import serializers
from .models import Movie, Genre, Cast, Review

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["id", "name"]

# 영화 목록: 장르 id 목록 포함
class MovieListSerializer(serializers.ModelSerializer):
    genres = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = [
            "id", "title", "release_date", "popularity",
            "budget", "revenue", "runtime",
            "genres"
        ]

class CastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cast
        fields = ["id", "name", "character", "order"]

# Review 목록/상세 공통
class ReviewSerializer(serializers.ModelSerializer):
    rating = serializers.FloatField(required=True)
    author = serializers.CharField(required=True)
    class Meta:
        model = Review
        fields = ["id", "movie", "author", "content", "rating"]
        read_only_fields = ["movie"]  # 영화 상세/작성 뷰에서 set

# 리뷰 목록에서 movie는 id, title만
class MovieTinySerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ["id", "title"]

class ReviewListSerializer(serializers.ModelSerializer):
    movie = MovieTinySerializer(read_only=True)
    class Meta:
        model = Review
        fields = ["id", "movie", "author", "content", "rating"]

# 영화 상세: cast_set, review_set 전체, genres의 name
class MovieDetailSerializer(serializers.ModelSerializer):
    cast_set = CastSerializer(many=True, read_only=True)
    review_set = ReviewSerializer(many=True, read_only=True)
    genres = serializers.SerializerMethodField()

    def get_genres(self, obj):
        return [ {"name": genre.name} for genre in obj.genres.all() ]

    class Meta:
        model = Movie
        fields = [
            "id", "title", "release_date", "popularity",
            "budget", "revenue", "runtime",
            "genres", "cast_set", "review_set",
        ]
