from rest_framework import serializers
from .models import Product, WishList, User
from categories.models import Category
from categories.serializers import CategorySerializer


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'


class WishListSerializer(serializers.ModelSerializer):
    wish_count = serializers.IntegerField(source='my_wishlist.count', read_only=True)
    products = ProductSerializer(many=True, read_only=True, source='wishlist')

    class Meta:
        model = User
        fields = ('username', 'wish_count', 'products',)
