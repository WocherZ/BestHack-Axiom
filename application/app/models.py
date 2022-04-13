from django.urls import reverse
from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=19, decimal_places=2, validators=[MinValueValidator(0)], default=0.0)



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
    ], )

    def __str__(self):
        return str(str(self.user) + ": " + str(self.price))
