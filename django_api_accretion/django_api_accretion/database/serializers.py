from rest_framework import serializers 
from .models import DeedRecords 

class DeedRecordsSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = DeedRecords 
        fields = '__all__' 