from rest_framework import serializers
from .models import ContactInfo 

class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = ["name", "email", "phone_number", "message"] 