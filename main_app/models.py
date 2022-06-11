from django.db import models

class Jewelry(models.Model):
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    category = models.CharField(max_length=250)
    description = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name

class Cart(models.Model):
    username = models.CharField(max_length=100)
    item_id = models.CharField(max_length=250)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.username + ', ' + self.username
