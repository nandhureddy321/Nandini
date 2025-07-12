from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=50)
    join_date = models.DateField()

    def __str__(self):
        return self.name
# Create your models here.
