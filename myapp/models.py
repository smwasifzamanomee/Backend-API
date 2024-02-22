from django.db import models

# Create your models here.

class Passanger(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Vehicle(models.Model):
    name = models.CharField(max_length=200)
    passanger = models.ForeignKey(Passanger, on_delete=models.CASCADE, related_name="Vehicle")
    
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    
    class Meta:
        indexes = [
            models.Index(fields=['title'])
        ]
    