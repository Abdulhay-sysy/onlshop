from rest_framework import serializers
from .models import Product
from category.models import Category
from category.serializers import CategorySerializer




class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = ['id','name', 'price','category','start_date','end_date']

    def create(self, validated_data):
        category_data = validated_data.pop('category')
        # Assuming that the Category model has an unique field such as name or id
        category, _ = Category.objects.get_or_create(name=category_data['name'])
        product = Product.objects.create(category=category, **validated_data)
        return product