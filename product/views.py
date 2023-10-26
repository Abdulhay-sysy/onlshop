from django.shortcuts import render
from .models import Product
from django.utils import timezone
from items.models import Items
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Sum
from .serializers import ProductSerializer
from rest_framework import generics

class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductCreate(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductUpdate(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDestroy(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductRetrive(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class TotalInventoryPrice(APIView):
    queryset = Product.objects.all()
    
    def get(self, request):
        total_price = Product.objects.aggregate(total=Sum('price'))
        return Response({"total_price": total_price['total']})
    
class ExpiredProducts(generics.ListAPIView):   
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter(end_date__lt=timezone.now())
    
class MostSoldProductView(APIView):
    
    def get(self, request, format=None):
        group_sale = Items.objects.values('product__name').annotate(total_quantity=Sum('quantity')).order_by('-total_quantity')
        
        most_sold = group_sale.first()

        if most_sold:
            most_sold_product_name = most_sold['product__name']
            
            data = {'kop sotilgan mahsulot': most_sold_product_name}
            
            return Response(data)
        else:
            return Response({'error': 'Xatolik'})