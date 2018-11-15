from django.db import models
from django.contrib.auth.models import User
import datetime
from versatileimagefield.fields import VersatileImageField

# Create your models here.

class Product(models.Model):
    """Django data model Product"""
    title = models.CharField(blank=True, max_length=100)
    url = models.TextField(blank=True)
    pub_date = models.DateTimeField(blank=True, default=datetime.datetime.now)
    votes_total = models.IntegerField(blank=True, null=True)
    product_pic = VersatileImageField(upload_to='product_pics/', height_field="150", width_field="150")
    icon_pic = VersatileImageField(upload_to="icon_pics/", height_field="50", width_field="50")
    body = models.TextField(default=1)
    hunter = models.ForeignKey(User ,on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


    def __str__(self):
        return str(self.title)

    def summary(self):
        return self.body[:70]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
