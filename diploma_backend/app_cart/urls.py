from django.contrib import admin
from django.urls import path, include

from app_cart.views import CartView


app_name = 'app_cart'

urlpatterns = [
    path('basket', CartView.as_view(), name='cart'),
]


