from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register('product',views.ProductViewSet,basename='product')
router.register('review',views.ProductReviewSet,basename='review')
router.register('doctorinfo',views.DoctorViewset,basename='doc_info')
router.register('order',views.OrderViewSet,basename='order')
# router.register('client/reg',views.ClientRegistraton,basename='c_registration')
# router.register('client/login',views.ClientLogin,basename='c_login')

urlpatterns = [
   path('',include(router.urls)),
   path('register',views.ClientRegistraton.as_view(),name='c_registration'),
   path('login',views.ClientLogin.as_view(),name='c_login'),

]