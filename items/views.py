from django.shortcuts import render
from .models import Items
from .serializers import ItemsSerializer
from rest_framework import generics

class ItemDetailView(generics.RetrieveAPIView):
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer

class ItemCreateView(generics.CreateAPIView):
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer

class ItemUpdateView(generics.UpdateAPIView):
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer

class ItemListView(generics.ListAPIView):
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer

class ItemDeleteView(generics.DestroyAPIView):
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer

class UserPurchasesView(generics.ListAPIView):
    serializer_class = ItemsSerializer

    def get_queryset(self):
       user_id = self.kwargs['user_id']
       return Items.objects.filter(shop_cart__customer=user_id)