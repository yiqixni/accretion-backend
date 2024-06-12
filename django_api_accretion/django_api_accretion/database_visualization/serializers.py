import os 
from dotenv import load_dotenv 
from rest_framework import serializers 
from .models import PropertyData 

load_dotenv()
host_domain = os.getenv('DOMAIN_GET_PNG')

class PropertyDataSerializer(serializers.ModelSerializer):
    class Meta: 
        model = PropertyData 
        fields = ['data'] 
        
class PropertyDataImageLinkSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = PropertyData 
        fields = ['imageLink'] 
        
class PropertyDataForView(serializers.ModelSerializer): 
    class Meta: 
        model = PropertyData 
        fields = ['data', 'imageLink'] 
    
    def to_representation(self, instance): #modify the imageLink to contain the full URL address 
        representation = super().to_representation(instance)
        request = self.context.get('request')
        if request:
            # representation['imageLink'] = request.build_absolute_uri(instance.imageLink)
            representation['imageLink'] = host_domain + (instance.imageLink)
        return representation 