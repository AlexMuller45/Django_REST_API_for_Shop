from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from rest_framework import routers

from app_users.views import UserViewSet, PasswordUpdateView, AvatarUpdateView

app_name = 'app_users'

urlpatterns = [
    path('profile', UserViewSet.as_view(), name='profile'),
    path('profile/password', PasswordUpdateView.as_view(), name='password'),
    path('profile/avatar', AvatarUpdateView.as_view(), name='avatar'),
    path('profile/avatar', AvatarUpdateView.as_view(), name='avatar'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

