from rest_framework.viewsets import ViewSet, ReadOnlyModelViewSet, ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from taggit.models import Tag
from django.db.models import Prefetch

from app_megano.models import Category, Subcategories, Products
from app_megano.serializers import CategorySerializer, TagsSerializer, ProductSerializer
from app_megano.paginations import ProductPagination


def set_query_limit(queryset, limit):
    if limit:
        queryset = queryset.all()[:limit]
    else:
        queryset = queryset.all()[:20]
    return queryset


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


class BaseCatalogViewSet(ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = (
        Products.objects
        .prefetch_related()
        .order_by('date')
    )
    search_field = ['category__title', 'title', 'description', 'fullDescription']
    serializer_class = ProductSerializer
    pagination_class = ProductPagination

    def get_queryset(self):
        category = self.request.query_params.get('category', None)
        product_sort = self.request.query_params.get('sort', None)
        product_sort_type = self.request.query_params.get('sortType', None)

        if category:
            self.queryset = self.queryset.filter(category=category)
        if product_sort:
            self.queryset = self.queryset.order_by(product_sort)
            if product_sort_type == 'inc':
                self.queryset = self.queryset.reverse()
        return self.queryset


class CatalogViewSet(BaseCatalogViewSet):

    def get_queryset(self):
        product_limit = self.request.query_params.get('limit', None)
        queryset = set_query_limit(super().queryset, product_limit)
        return queryset


class CatalogByCategoryViewSet(BaseCatalogViewSet):

    def get_queryset(self):
        product_limit = self.request.query_params.get('limit', None)
        queryset = super().queryset.filter(category=self.kwargs['pk'])
        queryset = set_query_limit(queryset, product_limit)
        return queryset

