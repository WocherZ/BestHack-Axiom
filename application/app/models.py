from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator


class User(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=64)
    name = models.CharField(max_length=32)

    balance = models.DecimalField(max_digits=19, decimal_places=2,  validators=[
            MinValueValidator(0)
        ],)

    def __str__(self):
        return str(self.name)


class Stock(models.Model):
    name = models.CharField(max_length=64)
    current_price = models.DecimalField(max_digits=19, decimal_places=2)
    slug = models.SlugField(max_length=255, unique=True, verbose_name="Ссылка")

    def get_absolute_url(self):
        return reverse('stock', kwargs={'stock_slug': self.slug})

    def __str__(self):
        return str(self.name)


class Properties(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.SET_NULL,
                                null=True)
    stock = models.OneToOneField(Stock,
                                 on_delete=models.SET_NULL,
                                 null=True)
    price = models.DecimalField(max_digits=19, decimal_places=2)
    number = models.IntegerField(validators=[
            MinValueValidator(0)
        ],)

    def __str__(self):
        return str(str(self.user) + ": " + str(self.price))

