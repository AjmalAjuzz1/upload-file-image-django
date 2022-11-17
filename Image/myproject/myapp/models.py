from django.db import models

# Create your models here.


class Image(models.Model):
    
    
    title = models.CharField(
        max_length=100,
        
    )
    description = models.CharField(
        max_length=200,
       
    )
    image = models.ImageField(upload_to='images')

    date = models.DateField(
        
    )

    