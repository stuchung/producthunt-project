from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone
from versatileimagefield.fields import VersatileImageField

# Create your models here.

class Product(models.Model):
    """Django data model Product"""
    title = models.CharField(blank=True, max_length=100)
    url = models.TextField(blank=True)
    pub_date = models.DateTimeField(default=timezone.now)
    votes_total = models.IntegerField(default=1)
    product_pic = VersatileImageField(upload_to='product_pics/')
    icon_pic = VersatileImageField(upload_to="icon_pics/")
    body = models.TextField(blank=True)
    hunter = models.ForeignKey(User ,on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['-pub_date']


    # def __str__(self):
    #     return self.title
    def __str__(self):
        return (self.title)

    def summary(self):
        return self.body[:70]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
