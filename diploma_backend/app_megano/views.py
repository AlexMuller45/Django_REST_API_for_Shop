from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Category, Subcategories
from .serializers import CategorySerializer
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
