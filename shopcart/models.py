from django.db import models
from customer.models import Customer
import uuid
from django.utils import timezone

class ShoppingCart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    CHOICES = (
        ('Cash', 'Cash'),
        ('Card', 'Card'),
    )
    date = models.DateTimeField(default=timezone.now)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    payment = models.CharField(max_length=20, choices=CHOICES, null=True, blank=True)
    
    def total(self):
        items = self.items.all()
        total = sum([item.product.price * item.quantity for item in items])
        return total
    def __str__(self):
        return self.customer.name 