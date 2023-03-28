from django.db import models

from app_megano.models import Products, Category


class CartItems(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    item_id = models.CharField(max_length=64, unique=True, null=False, blank=False, verbose_name='ID товара')
    category = models.CharField(max_length=16, unique=True, null=False, blank=False, verbose_name='ID категории')
    price = models.DecimalField(max_digits=9, decimal_places=2, default=0, verbose_name='Стоимость единицы товара')
    count = models.PositiveSmallIntegerField(default=0, verbose_name='Количество товара')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления товара')
    freeDelivery = models.BooleanField(default=False, verbose_name='Бесплатная доставка есть/нет')

    # def __str__(self):
    #     obj = Products.objects.get(pk=int(self.item_id)).values('title')
    #     return obj.title

