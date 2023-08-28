from django.urls import path

from .views import (ProductDetailApiView,
                    ProductListApiView, CategoryListApiView)

urlpatterns = [
    path('all/', ProductListApiView.as_view(), name='product_list'),
    path('u/<str:username>/<slug:product_slug>/',
         ProductDetailApiView.as_view(), name='product_detail'),
    path('categories/', CategoryListApiView.as_view(), name='category_list')
]
