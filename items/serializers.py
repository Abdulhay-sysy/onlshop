from rest_framework import serializers
from .models import Product
from .models import ShoppingCart
from product.models import Product
from category.serializers import CategorySerializer
from .models import Items


class ItemsSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    shop_cart = serializers.PrimaryKeyRelatedField(queryset=ShoppingCart.objects.all())

    class Meta:
        model = Items
        fields = ['id','product','shop_cart','sell_date','quantity']

    def create(self, validated_data):

        return Items.objects.create(**validated_data)
