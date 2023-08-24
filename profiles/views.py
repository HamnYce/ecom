from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
import rest_framework.status as status
from .serializers import UserProfileSerializer
from .models import UserProfile
from .paginators import UserProfilePaginator

# Create your views here.


class UserProfileListApiView(APIView):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = UserProfilePaginator()

    # list user profiles
    def get(self, request, *args, **kwargs):
        queryset = UserProfile.objects.all()
        page = self.pagination_class.paginate_queryset(
            queryset=queryset, request=request)
        if page is not None:
            serializer = UserProfileSerializer(page, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        serializer = UserProfileSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # create new profile (for new user)
    def post(self, request, *args, **kwargs):
        pass


class UserProfileDetailApiView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # get specific user profile with username
    def get(self, request, *args, **kwargs):
        # username = UserProfile.objects.filter(email=request.user.email)
        print(request.user.email)
        return Response(status=status.HTTP_200_OK)

    # update existing user profile
    # requires the user updating have the same email as the user being udpated
    def put(self, request, *args, **kwargs):
        pass
