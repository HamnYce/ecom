from rest_framework import serializers
from .models import UserProfile


class ReadUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        exclude = ['user']


#
class WriteUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        exclude = ['user', 'gender']
