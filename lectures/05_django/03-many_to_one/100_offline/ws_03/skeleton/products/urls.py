from django.urls import path
from . import views

urlpatterns = [
    path("", views.product_list),
    path('<int:category_pk>/', views.create_product),


]