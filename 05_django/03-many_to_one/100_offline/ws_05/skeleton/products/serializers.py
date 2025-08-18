from rest_framework import serializers
from .models import Product
from categories.models import Category
from categories.serializers import CategorySerializer


class ProductSerializers(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'