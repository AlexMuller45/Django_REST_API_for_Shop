from rest_framework import serializers

from app_megano.models import Products, Category


class ProductSerializer(serialiser.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meya:
        model = Category
        fields = '__all__'


