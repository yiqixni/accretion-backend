from rest_framework import serializers 
from .models import PropertyData 

class PropertyDataSerializer(serializers.ModelSerializer):
    class Meta: 
        model = PropertyData 
        fields = ['data'] 