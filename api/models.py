from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    password = models.CharField('password', max_length=128, blank=True)


class Product(models.Model):
    name = models.CharField(max_length=1024, blank=True, null=True, verbose_name='Product Name')
    media = models.TextField(blank=True, null=True, verbose_name='Media')
    description = models.TextField(blank=True, null=True, verbose_name='Description')
    amount = models.DecimalField(default=0, blank=True, null=True, verbose_name='Amount', max_digits=10,
                                 decimal_places=2, max_length=13)
