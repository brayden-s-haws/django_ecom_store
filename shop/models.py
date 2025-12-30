from django.db import models

# Create your models here.
class Product(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=200)
    price = models.FloatField()
    discounted_price = models.FloatField()
    image = models.CharField(max_length=300)


class Order(models.Model):

    def __str__(self):
        return f"Order ID {self.id}"

    items = models.CharField(max_length=1000)
    total = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
