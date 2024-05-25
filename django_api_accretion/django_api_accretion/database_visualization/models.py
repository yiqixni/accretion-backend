from django.db import models

# Deed record database based on Attoms ID  
class PropertyData(models.Model): 
    propertyID = models.CharField(max_length=255, unique=True) 
    query_string = models.CharField(max_length=255) 
    data = models.JSONField() 
    imageLink = models.URLField(blank=True, null=True)
    
    def __str__(self): 
        return self.propertyID 