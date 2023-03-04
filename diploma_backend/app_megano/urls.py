from typing import Any, List

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from .views import CategoriesViewSet

urlpatterns = [
    path('categories/', CategoriesViewSet.as_view({'get': 'list'}))
]
