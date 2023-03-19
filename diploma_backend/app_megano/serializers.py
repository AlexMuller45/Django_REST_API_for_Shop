from rest_framework import serializers

from app_megano.models import Products, Category


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'


class SubcategorySerializer(serializers.ModelSerializer):
    href = serializers.CharField(source='get_absolute_url', read_only=True)
    image = serializers.SerializerMethodField()
    id = str('id')

    class Meta:
        model = Category
        fields = ['id', 'title', 'image', 'href']

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['id'] = str(repr['id'])
        return repr

    def get_image(self, obj):
        return {'src': obj.image_src.url, 'alt': obj.image_alt}


class CategorySerializer(serializers.ModelSerializer):
    href = serializers.CharField(source='get_absolute_url', read_only=True)
    subcategories = SubcategorySerializer(many=True, read_only=True)
    image = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'title', 'href', 'image', 'subcategories']

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['id'] = str(repr['id'])
        return repr

    def get_image(self, obj):
        return {'src': obj.image_src.url, 'alt': obj.image_alt}


