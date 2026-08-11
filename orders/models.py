from django.db import models
from products.models import Product

class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    email = models.EmailField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer_name