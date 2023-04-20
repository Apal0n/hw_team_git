from django.db import models


class Order(models.Model):
    name = models.CharField(max_length=30)
    price = models.CharField(max_length=30)
    quantity = models.CharField(max_length=30)
    courier = models.ForeignKey('Courier', on_delete=models.CASCADE, related_name='orders')

    def __str__(self):
        return self.name
