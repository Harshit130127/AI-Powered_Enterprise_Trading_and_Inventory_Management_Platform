from django.db import models

# Create your models here.


class product(models.Model):

    name=models.CharField(max_length=200)
    sku=models.CharField(max_length=100,unique=True) # sku means stock keeping unit, used internally by the company to track inventory
    description  =models.TextField(blank=True)
    current_stock= models.IntegerField(default=0)
    purchase_cost = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering= ['-created_at']

        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['sku'])
        ]


    def __str__(self):
        return f"{self.name} ({self.sku})"


