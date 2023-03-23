from django.conf.urls.static import static
from django.urls import path
from django.conf import settings
from rest_framework import routers

from .views import UserViewSet

app_name = 'app_users'


urlpatterns = [
    path('profile', UserViewSet.as_view(), name='profile'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

