from django.shortcuts import render
from .models import ShoppingCart
from rest_framework.response import Response
from rest_framework.views import APIView
from customer.models import Customer
from product.models import Product
from .serializers import ShoppingCartSerializer
from rest_framework import generics

class ShoppingCartList(generics.ListAPIView):
    queryset = ShoppingCart.objects.all()
    serializer_class = ShoppingCartSerializer

class ShoppingCartCreate(generics.CreateAPIView):
    queryset = ShoppingCart.objects.all()
    serializer_class = ShoppingCartSerializer

class ShoppingCartUpdate(generics.UpdateAPIView):
    queryset = ShoppingCart.objects.all()
    serializer_class = ShoppingCartSerializer

class ShoppingCartDestroy(generics.DestroyAPIView):
    queryset = ShoppingCart.objects.all()
    serializer_class = ShoppingCartSerializer

class ShoppingCartRetrieve(generics.RetrieveAPIView):
    queryset = ShoppingCart.objects.all()
    serializer_class = ShoppingCartSerializer

class PriceCountAPIView(APIView):
    queryset = ShoppingCart.objects.all()

    def get(self, request, customer_id):
        customer = Customer.objects.get(id=customer_id)
        shopping_carts = ShoppingCart.objects.filter(customer_id=customer_id)
        expensive_products = Product.objects.filter(Q(id__in=[item.product_id for cart in shopping_carts for item in cart.items.all()]) & Q(price__gt=100))
        total_price = sum(product.price for product in expensive_products)
        total_million = 'Mijozning umumiy haridi 1000000 so\'mdan oshgan' if total_price > 1000000 else 'Mijozning umumiy haridi 1000000 so\'mdan oshmagan'
            
        return Response({"customer_name": customer.name, "count": expensive_products.count(), "total_price": total_price, 'Natija': total_million})
