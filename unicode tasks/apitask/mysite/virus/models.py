from django.db import models

# Create your models here.
# we create a model and then register it to admin
class COUNTRY(models.Model):
    cname= models.CharField(max_length=100)    
    name= models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    
    def __str__(self):
        return self.name


         
 