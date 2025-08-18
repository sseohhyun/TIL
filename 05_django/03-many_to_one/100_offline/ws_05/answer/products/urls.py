from django.urls import path
from . import views

urlpatterns = [
    path("", views.product_list),
    path('<int:category_pk>/', views.create_product),
    path('<int:product_pk>/<int:user_pk>/', views.add_wishlist),
    path('wishlist/<int:user_pk>/', views.wishlist)


]