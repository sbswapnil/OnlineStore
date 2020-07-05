from django.db import models
from datetime import datetime
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()


class Department(models.Model):
    department = models.CharField(max_length=20, unique=True)

    class Meta:
        ordering = ("department",)

    def __str__(self):
        return self.department

    objects = models.Manager()


class ProductCatagory(models.Model):
    department = models.ForeignKey(to=Department, on_delete=models.CASCADE, default=1)
    category = models.CharField(max_length=20, unique=True)
    objects = models.Manager()

    class Meta:
        ordering = ("category",)

    def __str__(self):
        return self.category


class Product(models.Model):
    units = (
        ('gm', 'gm'),
        ('kg', 'kg'),
        ('liter', 'liter'),
        ('dozens', 'dozens'),
        ('unit', 'unit'),
    )
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, unique=True)
    category = models.ForeignKey(to=ProductCatagory, on_delete=models.CASCADE, default=1)
    quantity = models.FloatField(default=0.0)
    price = models.FloatField(default=0.0)
    unit = models.CharField(max_length=20, choices=units, default='kg')
    offer = models.BooleanField(default=False)
    percent = models.IntegerField(default=0)
    img = models.ImageField(upload_to="Product/")

    date_updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name

    objects = models.Manager()


class Banner(models.Model):
    name = models.CharField(max_length=20)
    discription = models.TextField()
    img = models.ImageField(upload_to="Banners/")

    def __str__(self):
        return self.name

    objects = models.Manager()
