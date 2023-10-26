from .models import Customer
from rest_framework import serializers

class CustomerSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Customer
        fields = ['id','location','name','phone','address']