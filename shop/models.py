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
