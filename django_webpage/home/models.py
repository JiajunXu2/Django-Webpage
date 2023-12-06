from django.db import models

# Create your models here.
class customer(models.Model):
    pass

class order(models.Model):
    pass

class order_item(models.Model):
    pass

class product(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()

class shipping_address(models.Model):
    address1 = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=7)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)