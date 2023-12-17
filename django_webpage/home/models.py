from django.db import models

# Create your models here.
class customer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    phone_number = models.FloatField()

class order(models.Model):
    client = models.ForeignKey(customer, on_delete=models.CASCADE)
    date = models.FloatField()

class product(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()

class order_item(models.Model):
    item = models.ForeignKey(product, on_delete=models.CASCADE)

class shipping_address(models.Model):
    client = models.ForeignKey(customer, on_delete=models.CASCADE)
    address1 = models.CharField(max_length=50)
    apt_number = models.CharField(max_length = 4)
    zip_code = models.FloatField()
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)