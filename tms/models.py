from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')

    def __str__(self):
        return f'{self.title}'


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return f'{self.name}'


class Cart(models.Model):
    product = models.ManyToManyField(Product, verbose_name='Продукт')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=User, verbose_name='Пользователь')
    total_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return f'{self.total_price}'
