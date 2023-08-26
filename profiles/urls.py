from django.urls import path
from .views import (UserProfileListApiView, UserProfileDetailApiView)

urlpatterns = [
    path('all/', UserProfileListApiView.as_view(), name='profile_list'),
    path('u/<str:username>/', UserProfileDetailApiView.as_view(),
         name='product_detail')
]
