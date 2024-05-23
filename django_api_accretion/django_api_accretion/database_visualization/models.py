from django.db import models

# Deed record database based on Attoms ID  
class PropertyData(models.Model): 
    propertyID = models.CharField(max_length=255, unique=True) 
    data = models.JSONField() 
    
    def __str__(self): 
        return self.propertyID 