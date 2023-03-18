from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Category, Subcategories
from .serializers import CategorySerializer


class CategoriesViewSet(ReadOnlyModelViewSet):

    queryset = Category.objects.select_related().all()
    serializer_class = CategorySerializer
