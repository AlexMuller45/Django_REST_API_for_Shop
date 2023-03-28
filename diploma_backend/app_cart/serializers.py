from rest_framework import serializers
from app_megano.models import Products, ProductImages
from app_cart.models import CartItems
from app_cart.CartServices import CartService


class CartSerializer(serializers.Serializer):
    id = serializers.CharField(source='item_id', read_only=True)
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    href = serializers.SerializerMethodField()
    images = serializers.SerializerMethodField()
    tags = serializers.SerializerMethodField()
    reviews = serializers.SerializerMethodField()
    rating = serializers.SerializerMethodField()

    class Meta:
        model = CartItems
        fields = ['id', 'category', 'price', 'count', 'date', 'title', 'description',
                  'href', 'freeDelivery', 'images', 'tags', 'reviews', 'rating']

    def get_title(self, obj):
        product = Products.objects.get(pk=int(obj.item_id)).values('title')
        return product.title

    def get_description(self, obj):
        product = Products.objects.get(pk=int(obj.item_id)).values('description')
        return product.description

    def get_href(self, obj):
        product = Products.objects.get(pk=int(obj.item_id)).values('href')
        return product.href

    def get_image(self, obj):
        images =  (
            ProductImages.objects
            .filter(product=int(obj.item_id))
            .values_list('imageURL', flat=True)
        )
        return images

    def get_tags(self, obj):
        product = Products.objects.get(pk=int(obj.item_id)).values('tags')
        return product.tags

    def get_reviews(self, obj):
        pass

    def get_rating(self, obj):
        pass

