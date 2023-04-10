from django.contrib import admin
from django.urls import path

from app_orders.views import OrdersViewSet


app_name = 'app_orders'


urlpatterns = [
    path('orders', OrdersViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='orders'),
    ]

