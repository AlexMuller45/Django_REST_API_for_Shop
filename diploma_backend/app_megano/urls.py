from typing import Any, List

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from app_megano.views import CategoriesViewSet, TagsViewSet, CatalogViewSet, CatalogByCategoryViewSet


app_name = 'app_megano'


urlpatterns = [
    path('categories', CategoriesViewSet.as_view({'get': 'list'}), name='categories'),
    path('tags', TagsViewSet.as_view({'get': 'list'}), name='tags'),
    path('catalog', CatalogViewSet.as_view({'get': 'list'}), name='catalog'),
    path('catalog/<int:pk>', CatalogByCategoryViewSet.as_view({'get': 'list'}), name='catalog_by_category'),
]
