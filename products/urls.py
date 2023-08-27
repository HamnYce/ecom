from django.urls import path

from .views import ProductDetailApiView, ProductListApiView

urlpatterns = [
    path('all/', ProductListApiView.as_view(), name='product_list'),
    path('u/<str:username>', ProductDetailApiView.as_view(), name='product_detail')
]
