from rest_framework import serializers
from django.contrib.auth.models import User

from .models import UserProfile


class UserSerializer(serializers.ModelSerializer):
    fullName = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField()
    avatar = serializers.CharField()

    class Meta:
        model = UserProfile
        fields = ['fullName', 'email', 'phone', 'avatar']
