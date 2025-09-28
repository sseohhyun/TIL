from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Movie, Genre, Review
from .serializers import (
    GenreSerializer, MovieListSerializer, MovieDetailSerializer,
    ReviewListSerializer, ReviewSerializer
)

# F02 전체 장르 목록
@api_view(["GET"])
def genre_list(request):
    genres = Genre.objects.all().order_by("id")
    return Response(GenreSerializer(genres, many=True).data)

# F03 전체 영화 목록 (장르 id 목록 포함)
@api_view(["GET"])
def movie_list(request):
    movies = Movie.objects.prefetch_related("genres").order_by("id")
    return Response(MovieListSerializer(movies, many=True).data)

# F04 단일 영화 상세 (cast/review/genres name 포함)
@api_view(["GET"])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie.objects.prefetch_related(
        "genres", "casts", "reviews"
    ), pk=movie_pk)
    return Response(MovieDetailSerializer(movie).data)

# F05 전체 리뷰 목록 (movie는 id/title만 포함)
@api_view(["GET"])
def review_list(request):
    qs = Review.objects.select_related("movie").order_by("id")
    return Response(ReviewListSerializer(qs, many=True).data)

# F06 단일 리뷰 조회/수정/삭제
@api_view(["GET", "PUT", "PATCH", "DELETE"])
def review_detail(request, review_pk):
    review = get_object_or_404(Review.objects.select_related("movie"), pk=review_pk)

    if request.method == "GET":
        return Response(ReviewListSerializer(review).data)


    if request.method == "PUT":
        serializer = ReviewSerializer(review, data=request.data)  # partial=False (기본)
        if serializer.is_valid():
            serializer.save()
            # movie 정보 포함된 serializer로 반환
            return Response(ReviewListSerializer(review).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "PATCH":
        serializer = ReviewSerializer(review, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(ReviewListSerializer(review).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE
    pk = review.pk
    review.delete()
    return Response({"delete": f"{pk}번 째 리뷰가 정상적으로 삭제되었습니다."})

# F07 특정 영화에 대한 리뷰 생성
@api_view(["POST"])
def create_review_for_movie(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid():
        review = serializer.save(movie=movie)
        return Response(ReviewListSerializer(review).data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)