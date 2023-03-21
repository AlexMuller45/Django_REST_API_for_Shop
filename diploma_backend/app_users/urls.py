from django.conf.urls.static import static
from django.urls import path
from django.conf import settings

from .views import UserViewSet

app_name = 'app_users'


urlpatterns = [
    path('profile', UserViewSet.as_view({'get': 'retrieve'})),
    path('profile', UserViewSet.as_view({'post': 'update'})),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

