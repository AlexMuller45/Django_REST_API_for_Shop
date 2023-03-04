from django.db import models

from app_users.models import UserProfile, Cities, Address
from app_megano.models import Products


class Orders(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=PROTECT)
    createdAt = models.DateTimeField(auto_now_add=True, verbose_name='Дата оформления заказа')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата обновления заказа')
    deliveryType = models.ForeignKey(DeliveryType, on_delete=PROTECT)
    paymentType = models.ForeignKey(PaymentType, on_delete=PROTECT)
    totalCost = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name='Сумма заказа')
    status = models.ForeignKey(Status, on_delete=PROTECT)
    city = models.ForeignKey(Cities, on_delete=PROTECT)
    address = models.ForeignKey(Address, on_delete=PROTECT)


    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Заказ - {}'.format(self.id)

    def get_total_cost(self):
        """
        Получение общей стоимости заказа
        :return: totalCost: Decimal
        """
        return sum(item.get_cost() for item in self.items.all())


class ProductInOrder(models.Model):
    order = models.ForeignKey(Orders, on_delete=PROTECT)
    product = models.ForeignKey(Products, on_delete=PROTECT)
    price = models.DecimalField(max_digits=9, decimal_places=2, default=0, verbose_name='Стоимость единицы товара')
    count = models.PositiveSmallIntegerField(default=1, verbose_name='Количество товара в заказе')

    def get_cost(self):
        return self.price * self.quantity


class DeliveryType(models.Model):
    name = CharField(max_length=50, null=True, blank=False, verbose_name='Тип доставки')
    description = models.TextField(null=True, blank=True, verbose_name='Описание типа доставки')

    def __str__(self):
        return self.name


class Status(models.Model):
    name = CharField(max_length=50, null=True, blank=False, verbose_name='Статус')
    description = models.TextField(null=True, blank=True, verbose_name='Описание статуса')

    def __str__(self):
        return self.name


class PaymentType(models.Model):
    name = CharField(max_length=50, null=True, blank=False, verbose_name='Тип оплаты')
    description = models.TextField(null=True, blank=True, verbose_name='Описание типа оплаты')

    def __str__(self):
        return self.name

