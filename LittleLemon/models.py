from django.db import models

# Create your models here.

class Menu(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    inventory = models.SmallIntegerField()
    
    def __str__(self):
        return self.title
    