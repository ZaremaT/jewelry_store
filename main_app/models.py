from django.db import models

class Cat(models.Model):

    breed = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    description = models.TextField(max_length=500)
    verified_cat = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.breed

    class Meta:
        ordering = ['breed']