from rest_framework.viewsets import ReadOnlyModelViewSet
from taggit.models import Tag

from .models import Category, Subcategories, Products
from .serializers import CategorySerializer, TagsSerializer
from django.db.models import Prefetch


class CategoriesViewSet(ReadOnlyModelViewSet):
    queryset = (
        Category.objects
        .filter(active=True)
        .prefetch_related(
                Prefetch(
                        'subcategories',
                        queryset=(
                            Subcategories.objects
                            .filter(active=True))
                )
        )
    )
    serializer_class = CategorySerializer


class TagsViewSet(ReadOnlyModelViewSet):
    queryset = (
        Tag.objects
        .order_by('name')
    )
    serializer_class = TagsSerializer


