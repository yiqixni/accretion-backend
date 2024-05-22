from django.db import models

# Create your models here.
class DeedRecords(models.Model): 
    date = models.CharField(max_length=255) 
    street_name = models.CharField(max_length=255) 
    # street_number = models.CharField(max_length=255) 
    town = models.CharField(max_length=255) 
    type = models.CharField(max_length=255) 
    book_page = models.CharField(max_length=255) 