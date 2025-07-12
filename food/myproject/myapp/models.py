from django.db import models

# Create your models here.
class canteen(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='Menu/', blank=True, null=True)

    def __str__(self):
        return self.name



class Bakery(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='Items/', blank=True, null=True)

    def __str__(self):
        return self.name


class mess(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='list/', blank=True, null=True)

    def __str__(self):
        return self.name