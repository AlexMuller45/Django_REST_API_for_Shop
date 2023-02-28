from django.contrib.auth.models import User
from django.db import models


class Products(models.Model):
    category = models.ManyToManyField(Category, related_name='products')
    price = models.PositiveIntegerField()
    count = models.PositiveIntegerField()
    title = models.CharField(max_length=150, unique=True, null=False, blank=False)
    description = models.TextField()
    full_description = models.TextField()
    href = models.URLField(unique=True, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    tags = TaggableManager(blank=True)
    specification = models.ForeignKey(Specifications, on_delete=SET_NULL, null=True)

    def __str__(self):
        return self.title


def product_image(instance, filename):
    saved_file_name = instance.product + '_' + instance.id
    return 'images/product/{}.jpg'.format(saved_file_name)


def category_image(cat_id, pref):
    saved_file_name = pref + '_' + cat_id
    return 'images/category/{}.jpg'.format(saved_file_name)


class ProductImages(models.Model):
    product = models.ForeignKey(Products, on_delete=CASCADE)
    name = models.CharField(max_length=80, null=True, blank=True)
    imageURL = models.ImageField(upload_to=product_image)


class Specifications(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)
    value = models.TextField()


class Category(models.Model):
    title = models.CharField(max_length=150, unique=True, null=False, blank=False)
    href = models.URLField(unique=True, null=False, blank=False)
    image_src = models.ImageField(upload_to=category_image(self.id, 'src'))
    image_alt = models.ImageField(upload_to=category_image(self.id, 'alt'))
    subcategory = models.ManyToManyField(Subcategories, related_name='category')


class Subcategories(models.Model):
    title = models.CharField(max_length=150, unique=True, null=False, blank=False)
    href = models.URLField(unique=True, null=False, blank=False)
    image_src = models.ImageField(upload_to=category_image(self.id, 'src_sub'))
    image_alt = models.ImageField(upload_to=category_image(self.id, 'alt_sub'))


class Reviews(models.Model):
    product = models.ForeignKey(Products, on_delete=CASCADE)
    author = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=70, blank=True, null=True)
    text = models.TextField()
    rate = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)


