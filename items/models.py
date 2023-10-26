from django.db import models
from product.models import Product
from shopcart.models import ShoppingCart
from django.utils import timezone
import uuid

class Items(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    shop_cart = models.ForeignKey(ShoppingCart, related_name='items', on_delete=models.CASCADE)
    sell_date = models.DateTimeField(default=timezone.now)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"
