from django.db import models
from django.contrib.auth.models import User 

# Create SellInfo 
class PropertyInfo(models.Model):
    address = models.CharField(max_length=100)
    description = models.CharField(max_length=255) 
    asking_price = models.DecimalField(max_digits=10, decimal_places=2) 
    shares = models.IntegerField() 
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    username = models.CharField(max_length=100, null=True, blank=True)
    
class PropertyImage(models.Model):
    property_info = models.ForeignKey(PropertyInfo, 
                                      on_delete=models.CASCADE, 
                                      related_name="images")
    image = models.ImageField(upload_to="property_images/") 
    description = models.CharField(max_length=255, blank=True, default="")
    

    
