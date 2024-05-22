from rest_framework import serializers 
from .models import PropertyInfo, PropertyImage 

class PropertyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyImage
        fields = ["id","image", "description"] 
        

class PropertyInfoSerializer(serializers.ModelSerializer): 
    images = PropertyImageSerializer(many=True, read_only=True) 
    uploaded_images = serializers.ListField(child=serializers.ImageField(), 
                                            write_only=True)
    
    class Meta:
        model = PropertyInfo 
        fields = ["id", "address", "description", "asking_price", "shares", 
                  "images", "uploaded_images", 
                  "user", "username"]

    def create(self, validated_data): 
        uploaded_images = validated_data.pop("uploaded_images") 
        property_info = PropertyInfo.objects.create(**validated_data) 
        
        for image in uploaded_images:
            PropertyImage.objects.create(property_info=property_info, image=image) 
        
        return property_info    
    