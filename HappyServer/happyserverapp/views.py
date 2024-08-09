from django.shortcuts import render,redirect,get_object_or_404
from rest_framework.viewsets import ModelViewSet,ViewSet
from rest_framework import permissions,authentication
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Product,Review,DoctorsInfo,OrderModel,DoctorPermissonModel,Cart,CartItem
from .serializers import ProductSerializer,ReviewSerializer,DoctorInfoSerializer,ClientSerializer,OrderSerializer,CartItemSerializer,CartSerializer
from rest_framework.views import APIView,status
from rest_framework_simplejwt import authentication as auth
from django.contrib.auth import authenticate,login
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class ProductViewSet(ModelViewSet):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    
# class ProductReviewSet(ModelViewSet):
#     authentication_classes=[authentication.BaseAuthentication]
#     permission_classes=[permissions.IsAuthenticated]
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

class ProductReviewSet(ModelViewSet):
    authentication_classes = [auth.JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class DoctorViewset(ModelViewSet):
    authentication_classes=[authentication.BaseAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    queryset = DoctorsInfo.objects.all()
    serializer_class =DoctorInfoSerializer
    

class ClientRegistraton(APIView):
    def post(self,request,*args,**kwargs):
        serializer=ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ClientLogin(APIView):
    def post(self,request,*args,**kwargs):
        u_name=request.data.get('username')
        pswd=request.data.get('password')
        user=authenticate(request,username=u_name,password=pswd)
        if user:
            login(request,user)
            return Response({'message':'login successful'},status=status.HTTP_200_OK)
        return Response({'message':'invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)


class OrderViewSet(ModelViewSet):
    authentication_classes=[authentication.BaseAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    queryset=OrderModel.objects.all()
    serializer_class=OrderSerializer



class OrderPermissionViewSet(ModelViewSet):
    # authentication_classes=[authentication.BaseAuthentication]  
    permission_classes=[permissions.IsAuthenticated]
    queryset=DoctorPermissonModel.objects.all()
    serializer_class=OrderSerializer
        



# class CartView(APIView):
#     def post(self, request):
#         product_id = request.data.get('product_id') 

#         try:
#             product = Product.objects.get(id=product_id)
#         except Product.DoesNotExist:
#             return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

        
#         return Response({'message': 'Product added to cart'}, status=status.HTTP_201_CREATED)


class AddtoCart(APIView):
    def post(self,request,*args,**kwargs):
        product_id=request.data.get('product_id')
        quantity=request.data.get('quantity')

        session_key=request.session.session_key

        if not session_key:
            request.session.create()
        session_key=request.session.session_key

        cart,created=Cart.objects.get_or_creat(session_key=session_key)   
        product=get_object_or_404(product,id=product_id)
        cart_item, created=CartItem.objects.get_or_create(cart=cart,product=product)  

        if not created:
            cart_item.quantity+=int(quantity)
            cart_item.save()

        else:
            cart_item.quantity=int(quantity)
            cart_item.save()
        
        serializer=CartItemSerializer(cart_item)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CartView(APIView):
    def get(self,request,*args,**kwargs):
        if not request.session.session_id:
            request.session.create()

        session_key=request.session.session_key
        cart=Cart.objects.filter(session_key=session_key).first()

        if not cart:
            return Response({'message':'cart not found'},status=status.HTTP_404_NOT_FOUND)
        
        serializer=CartSerializer()
        return Response(serializer.data, status=status.HTTP_200_OK)







        
