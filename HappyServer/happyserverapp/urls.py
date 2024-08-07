from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register('product',views.ProductViewSet,basename='product')
router.register('review',views.ProductReviewSet,basename='review')
router.register('doctorinfo',views.DoctorViewset,basename='doc_info')

urlpatterns = [
   path('',include(router.urls)),
]