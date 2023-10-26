
from rest_framework import serializers
from .models import ShoppingCart
from customer.serializers import CustomerSerializer
from customer.models import Customer


class ShoppingCartSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()

    class Meta:
        model = ShoppingCart
        fields = ['id','customer','payment','date']

    def create(self, validated_data):
        customer_data = validated_data.pop('customer')
        customer = Customer.objects.create(**customer_data)
        shopping_cart = ShoppingCart.objects.create(customer=customer, **validated_data)
        return shopping_cart
