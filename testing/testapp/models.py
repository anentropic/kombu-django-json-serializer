from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=16)


class Example(models.Model):
    customer = models.ForeignKey(Customer)
    name = models.CharField(max_length=100)
    count = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    birthday = models.DateField(null=True)
    beer_o_clock = models.TimeField(null=True)
    price = models.DecimalField(null=True, max_digits=5, decimal_places=2)
