from django.db import models

# Create your models here.
class Shop(models.Model):
    name = models.CharField(max_length=64)
    address = models.CharField(max_length=128)

class Menu(models.Model):
    shop = models.ForeignKey(Shop,on_delete=models.CASCADE)
    food_name = models.CharField(max_length = 64)

class Order(models.Model):
    shop = models.ForeignKey(Shop,on_delete=models.CASCADE)
    order_date = models.DateTimeField('date ordered')
    address = models.CharField(max_length=128)
    delivery_finish = models.BooleanField(default=0)
    estimated_time = models.IntegerField(default=-1)
    test = models.CharField(max_length=128)
class OrderFood(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    food_name = models.CharField(max_length=64)
    