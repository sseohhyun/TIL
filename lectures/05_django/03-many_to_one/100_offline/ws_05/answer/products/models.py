from django.db import models
from categories.models import Category

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class User(models.Model):
    username = models.CharField(max_length=120)
    wishlist = models.ManyToManyField(Product, through='Wishlist', related_name='wishlists')

    def __str__(self):
        return self.username

class WishList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='my_wishlist')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.product.title}"
