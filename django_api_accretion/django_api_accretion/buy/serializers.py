from rest_framework import serializers
from .models import Buy 

class BuySerializer(serializers.ModelSerializer):
    class Meta:
        model = Buy
        fields = ['address', 'price', 'quantity', 'date']