from rest_framework import serializers
from .models import Product,Review,DoctorsInfo,OrderModel,Cart,CartItem
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

    def create(self,validated_data):
        user=User.objects.create_user(
            first_name = validated_data['first_name'],
            username = validated_data['username'],
            email = validated_data['email'],
            password = validated_data['password']
        )
        return user


# class DoctorPermissonSerializer(serializers.ModelSerializer);
#     class Meta:
#         model=DoctorPermissonModel
#         fields=[]

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=OrderModel
        # fields='__all__'
        exclude = ['user','status','date','permission']

    def create(self,validated_data):
        user = self.context['request'].user
        return OrderModel.objects.create(user=user, **validated_data)
        
    
    # def create(self,data):
    #     user = self.context['request'].user
    #     doctor_permission=data.get('doctor_permission')

    #     if 
    #     raise serializers.ValidationError('Doctor permission required for this product.')
        # return OrderModel.objects.create(user=user, **validated_data)


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cart
        fields='__all__'

    
class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=CartItem
        fields='__all__'
    

    
