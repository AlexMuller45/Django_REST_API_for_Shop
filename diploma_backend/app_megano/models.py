from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.db import models


def product_image(instance):
    """
    Генерация пути и имени файла для изображения продукта
    :param instance: экземпляр модели
    :return: filename: str
    """
    saved_file_name = instance.product + '_' + instance.id
    return 'images/product/{}.jpg'.format(saved_file_name)


def category_image(cat_id, type_img):
    """
    Генерация пути и имени файла для изображения каталога или подкаталога
    :param cat_id: id каталога или подкаталога
    :param type_img: тип изображения (основное или дополнительное)
    :return: filename: str
    """
    saved_file_name = type_img + '_' + str(cat_id)
    return 'images/category/{}.jpg'.format(saved_file_name)


class Subcategories(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150, unique=True, null=False, blank=False, verbose_name='Название подкатегории')
    href = models.URLField(unique=True, null=False, blank=False, verbose_name='Ссылка')
    image_src = models.ImageField(upload_to=category_image(id, 'src_sub'),
                                  verbose_name='Основное изображение')
    image_alt = models.ImageField(upload_to=category_image(id, 'alt_sub'),
                                  verbose_name='Альтернативное изображение')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Подкатегории'
        verbose_name = 'Подкатегория'


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150, unique=True, null=False, blank=False, verbose_name='Название категории')
    href = models.URLField(unique=True, null=False, blank=False, verbose_name='Ссылка')
    image_src = models.ImageField(upload_to=category_image(id, 'src'), verbose_name='Основное изображение')
    image_alt = models.ImageField(upload_to=category_image(id, 'alt'), verbose_name='Альтернативное изображение')
    subcategory = models.ManyToManyField(Subcategories, related_name='category', verbose_name='Подкатегории')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'


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

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Товары'
        verbose_name = 'Товар'


class ProductImages(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    name = models.CharField(max_length=80, null=True, blank=True, verbose_name='Название изображения')
    imageURL = models.ImageField(upload_to=product_image, verbose_name='Ссылка на изображение')

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

