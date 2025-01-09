from email.policy import default

from django.db import models


# Create your models here.
class products(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    stock = models.IntegerField()
    description = models.TextField(null=True)
    image_url = models.JSONField(blank=True, default=list)


''