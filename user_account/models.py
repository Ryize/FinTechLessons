from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=48, verbose_name='Название')
    description = models.TextField(verbose_name='Описание товара')
    price = models.PositiveIntegerField(verbose_name='Цена')
    amount = models.PositiveSmallIntegerField(verbose_name='Количество')
    created_at = models.DateTimeField(auto_now_add=True)
