
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import ProductSerializers
from rest_framework import status
from .models import Product, User
from categories.models import Category

# Create your views here.
@api_view(['GET'])
def product_list(request):
    products = get_list_or_404(Product)
    serializer = ProductSerializers(products, many=True)
    return Response(serializer.data)



@api_view(['POST'])
def create_product(request, category_pk):
    category = get_object_or_404(Category, pk=category_pk)
    product = ProductSerializers(data=request.data)
    if product.is_valid(raise_exception=True):
        product.save(category=category)
        return Response(product.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def wishlist(request, product_pk, user_pk):
    product = get_object_or_404(Product, pk=product_pk)
    user = get_object_or_404(User, pk=user_pk)

    if product in user.wishlist.all():
        user.wishlist.remove(product)
        return Response({f"message": f"찜 목록에서 {product.title}을 제거했습니다."}, status=status.HTTP_204_NO_CONTENT)
    else:
        user.wishlist.add(product)
        return Response({f"message": f"찜 목록에 {product.title}을 추가했습니다."}, status=status.HTTP_201_CREATED)