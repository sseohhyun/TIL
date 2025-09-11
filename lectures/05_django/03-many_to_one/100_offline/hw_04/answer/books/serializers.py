
from rest_framework import serializers
from .models import Book, Genre
from authors.models import Author


class BookSerializer(serializers.ModelSerializer):
    class AuthorSerializer(serializers.ModelSerializer):
        class Meta:
            model = Author
            fields = ('name',)
    author = AuthorSerializer()

    class Meta:
        model = Book
        fields = ('title', 'author',)


class GenreSerializer(serializers.ModelSerializer):

    books = BookSerializer(many=True, read_only=True)
    book_count = serializers.IntegerField(source='books.count', read_only=True)

    class Meta:
        model = Genre
        fields = ('name', 'books', 'book_count')