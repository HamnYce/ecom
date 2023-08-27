from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
import rest_framework.status as status
from .serializers import (ReadUserProfileSerializer,
                          WriteUserProfileSerializer)
from .models import UserProfile
from .paginators import UserProfilePaginator
from .permissions import HasProfileOrReadOnly

# Create your views here.


class UserProfileListApiView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = UserProfilePaginator()

    # list user profiles
    def get(self, request, *args, **kwargs):
        queryset = UserProfile.objects.all()
        page = self.pagination_class.paginate_queryset(
            queryset=queryset, request=request)
        if page is not None:
            serializer = ReadUserProfileSerializer(page, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        serializer = ReadUserProfileSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    from rest_framework.request import Request
    # create new profile (for new user)

    def post(self, request: Request, *args, **kwargs):
        data = request.data
        serializer = ReadUserProfileSerializer(data=data)
        if request.user.has_profile:
            return Response({'reason': 'user already has profile'}, status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            serializer.save(user=request.user)
            request.user.register_profile()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfileDetailApiView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly, HasProfileOrReadOnly]

    # get specific user profile with username
    def get(self, request, *args, **kwargs):
        username = kwargs['username']
        try:
            user_profile = UserProfile.objects.get(username=username)
        except UserProfile.DoesNotExist as e:
            return Response({'reason': 'user does not exist'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = ReadUserProfileSerializer(instance=user_profile)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # update existing user profile
    # requires the user updating have the same email as the user being udpated

    def put(self, request, *args, **kwargs):
        username = kwargs['username']
        if username != request.user.userprofile.username:
            return Response({'reason': 'can only edit own information'}, status=status.HTTP_401_UNAUTHORIZED)

        data = request.data

        serializer = WriteUserProfileSerializer(
            request.user.userprofile, data=data, partial=True
        )

        if serializer.is_valid():
            serializer.save()
            read_serializer = ReadUserProfileSerializer(
                instance=request.user.userprofile)
            return Response(read_serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
