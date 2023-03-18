from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.db import models

product_image_path = 'images/product/'
category_image_path = 'images/category/'


# def product_image(instance):
#     """
#     Генерация пути и имени файла для изображения продукта
#     :param instance: экземпляр модели
#     :return: filename: str
#     """
#     saved_file_name = instance.product + '_' + instance.id
#     return 'images/product/{}.jpg'.format(saved_file_name)
#
#
# def category_image(cat_id, type_img):
#     """
#     Генерация пути и имени файла для изображения каталога или подкаталога
#     :param cat_id: id каталога или подкаталога
#     :param type_img: тип изображения (основное или дополнительное)
#     :return: filename: str
#     """
#     saved_file_name = type_img + '_' + str(cat_id)
#     return 'images/category/{}.jpg'.format(saved_file_name)
#

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150, unique=True, null=False, blank=False, verbose_name='Название категории')
    # href = models.URLField(unique=True, null=True, blank=True, verbose_name='Ссылка')
    image_src = models.ImageField(upload_to=category_image_path, verbose_name='Основное изображение',
                                  null=True, blank=True)
    image_alt = models.ImageField(upload_to=category_image_path, verbose_name='Альтернативное изображение',
                                  null=True, blank=True)
    active = models.BooleanField(default=False, verbose_name='Aктивные категории товаров')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('catalog', args=[str(self.id)])

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'


class Subcategories(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category,
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 verbose_name='Категория товара')
    title = models.CharField(max_length=150, unique=True, blank=False, verbose_name='Название подкатегории')
    # href = models.URLField(unique=True, null=False, blank=False, verbose_name='Ссылка')
    image_src = models.ImageField(upload_to=category_image_path,
                                  verbose_name='Основное изображение',
                                  null=True, blank=True)
    image_alt = models.ImageField(upload_to=category_image_path,
                                  verbose_name='Альтернативное изображение',
                                  null=True, blank=True)
    active = models.BooleanField(default=False, verbose_name='Aктивные подкатегории товаров')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Подкатегории'
        verbose_name = 'Подкатегория'


class Specifications(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True, verbose_name='Характеристика')
    value = models.TextField(verbose_name='Значение характеристики')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Спецификации'
        verbose_name = 'Спецификация'


class Products(models.Model):
    category = models.ManyToManyField(Category, related_name='products')
    price = models.DecimalField(max_digits=9, decimal_places=2, default=0, verbose_name='Стоимость единицы товара')
    count = models.PositiveSmallIntegerField(default=0, verbose_name='Количество товара у продавца')
    title = models.CharField(max_length=150, unique=True, null=False, blank=False, verbose_name='Название товара')
    description = models.TextField(null=True, blank=True, verbose_name='Краткое описание товара')
    fullDescription = models.TextField(null=True, blank=True, verbose_name='Полное описание товара')
    freeDelivery = models.BooleanField(default=False, verbose_name='Бесплатная доставка есть/нет')
    href = models.URLField(unique=True, null=False, blank=False, verbose_name='Ссылка на страницу товара')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата оформления товара')
    date_update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления товара')
    tags = TaggableManager(blank=True)
    specification = models.ForeignKey(Specifications, on_delete=models.SET_NULL, null=True,
                                      verbose_name='Особенности товара')
    active = models.BooleanField(default=False, verbose_name='Aктивные категории товаров')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Товары'
        verbose_name = 'Товар'


class ProductImages(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    name = models.CharField(max_length=80, null=True, blank=True, verbose_name='Название изображения')
    imageURL = models.ImageField(upload_to=product_image_path, verbose_name='Ссылка на изображение')

    class Meta:
        verbose_name_plural = 'Изображения товара'
        verbose_name = 'Изображение товара'


class Reviews(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    author = models.CharField(max_length=100, null=False, blank=False, verbose_name='Автор')
    email = models.EmailField(max_length=70, blank=True, null=True)
    text = models.TextField(verbose_name='Текст отзыва')
    rate = models.IntegerField(verbose_name='Рейтинг отзыва')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления отзыва')
    date_update = models.DateTimeField(auto_now=True, verbose_name='Дата изменения отзыва')

    class Meta:
        verbose_name_plural = 'Отзывы'
        verbose_name = 'Отзыв'

    def update_rate(self):
        pass

