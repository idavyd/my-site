from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50,blank=False)
    price = models.DecimalField(decimal_places=2, max_digits=10000,blank=False)
    overview = models.TextField(blank=True)
    used = models.BooleanField(default=True)

class DroneProduct(models.Model):
    brand = models.CharField(max_length=30)
    model_name = models.CharField(max_length=30)
    date_added = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=4,decimal_places=2)
    description = models.TextField(max_length=100)








