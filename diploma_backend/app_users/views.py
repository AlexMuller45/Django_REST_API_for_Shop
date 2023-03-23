import json
from rest_framework.parsers import JSONParser
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .models import UserProfile
from .serializers import UserSerializer


class UserViewSet(APIView):
    permission_classes = (IsAuthenticated, IsAdminUser, )
    serializer_class = UserSerializer
    parser_classes = [JSONParser]

    def check_profile(self):
        if not UserProfile.objects.filter(user=self.request.user).exists():
            UserProfile.objects.create(user=self.request.user)

    def get_data(self):
        self.check_profile()
        profile = UserProfile.objects.get(user=self.request.user)
        return {
            'fullName': self.request.user.get_full_name(),
            'email': self.request.user.email,
            'phone': profile.phone,
            'avatar': profile.avatar}

    def get(self, request, *args, **kwargs):
        data = self.get_data()
        serializer = self.serializer_class(data)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        user = request.user
        profile = UserProfile.objects.get(user=request.user)
        instance = self.get_data()
        data = request.data
        serializer = self.serializer_class(instance=instance,
                                           data=data,
                                           partial=True)
        if serializer.is_valid():
            user.first_name, user.last_name = data['fullName'].split()
            user.email = data['email']
            profile.phone = data['phone']
            profile.avatar = data['avatar']
            user.save()
            profile.save()
        return Response(serializer.data)

