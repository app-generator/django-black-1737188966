# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Products(models.Model):

    #__Products_FIELDS__
    id = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    brand = models.CharField(max_length=255, null=True, blank=True)
    category = models.CharField(max_length=255, null=True, blank=True)
    url = models.CharField(max_length=255, null=True, blank=True)

    #__Products_FIELDS__END

    class Meta:
        verbose_name        = _("Products")
        verbose_name_plural = _("Products")


class Prices(models.Model):

    #__Prices_FIELDS__
    product_id = models.ForeignKey(products, on_delete=models.CASCADE)
    id = models.CharField(max_length=255, null=True, blank=True)
    prices = models.BooleanField()
    currency = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Prices_FIELDS__END

    class Meta:
        verbose_name        = _("Prices")
        verbose_name_plural = _("Prices")


class Stocks(models.Model):

    #__Stocks_FIELDS__
    id = models.CharField(max_length=255, null=True, blank=True)
    product_id = models.ForeignKey(products, on_delete=models.CASCADE)
    stock_status = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Stocks_FIELDS__END

    class Meta:
        verbose_name        = _("Stocks")
        verbose_name_plural = _("Stocks")


class Promotions(models.Model):

    #__Promotions_FIELDS__
    id = models.CharField(max_length=255, null=True, blank=True)
    product_id = models.ForeignKey(products, on_delete=models.CASCADE)
    discount = models.BooleanField()
    currency = models.CharField(max_length=255, null=True, blank=True)
    promotion_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    end_date = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Promotions_FIELDS__END

    class Meta:
        verbose_name        = _("Promotions")
        verbose_name_plural = _("Promotions")



#__MODELS__END
