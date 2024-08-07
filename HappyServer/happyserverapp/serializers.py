from rest_framework import serializers
from .models import Product,Review,DoctorsInfo
from django.contrib.auth.models import User
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields='__all__'

    
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'


class DoctorInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model=DoctorsInfo
        fields='__all__'


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['first_name','username','email','password']

    
