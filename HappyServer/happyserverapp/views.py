from django.shortcuts import render,redirect
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions,authentication
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Product,Review,DoctorsInfo
from .serializers import ProductSerializer,ReviewSerializer,DoctorInfoSerializer,ClientSerializer
from rest_framework.views import APIView,status
from django.contrib.auth import authenticate,login
# Create your views here.

class ProductViewSet(ModelViewSet):
    authentication_classes=[authentication.BaseAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class ProductReviewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    # @action(detail=True)
    # def like(self, request, pk=None):
    #     product = self.get_object()
    #     product.likes += 1
    #     product.save()
    #     serializer = self.get_serializer(product, many=False)
    #     return Response(serializer.data)

class DoctorViewset(ModelViewSet):
    queryset = DoctorsInfo.objects.all()
    serializer_class =DoctorInfoSerializer
    

class ClientRegistraton(APIView):
    def post(self,request,*args,**kwargs):
        serializer=ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class ClientLogin(APIView):
#     def post(self,request,*args,**kwargs):
#         username=request.data.get('username')
#         password=request.data.get('password')
#         user=authenticate(request,username=username)