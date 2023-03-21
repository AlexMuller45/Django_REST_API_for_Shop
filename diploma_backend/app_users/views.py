from django.contrib.auth.models import User
from rest_framework.viewsets import ViewSet
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from .models import UserProfile
from .serializers import UserSerializer


class UserViewSet(ViewSet):
    permission_classes = (IsAuthenticated, IsAdminUser, )
    serializer_class = UserSerializer

    def retrieve(self, request, *args, **kwargs):
        profile_data = UserProfile.objects.get(user=request.user)
        data = dict(
                fullName=' '.join([request.user.first_name, request.user.last_name]),
                email=request.user.email,
                phone=profile_data.phone,
                avatar=profile_data.avatar
        )
        serializer = self.serializer_class(data)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        pass

