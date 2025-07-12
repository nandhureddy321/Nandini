from django.db import models

class Member(models.Model):
    firstname = models.CharField(max_length=255) 
    lastname = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)    
    joined_date = models.DateField()  
    

    def __str__(self):
        return f"{self.firstname} {self.lastname} {self.phone} {self.joined_date}"