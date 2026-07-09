from django.db import models

# Create your models here.
from products.models import product


class Order(models.Model):

    product = models.ForeignKey(product, on_delete=models.CASCADE)
