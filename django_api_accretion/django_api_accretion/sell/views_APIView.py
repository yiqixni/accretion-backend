from django.shortcuts import render
from rest_framework.response import Response 
from rest_framework.views import APIView 
from rest_framework import status

# Create class-based APIViews here.
class Sell(APIView):
    def get(self, request):
        city = request.GET.get("city") 
        print(city)
        if city:
            return Response({"message": f"browse your current properties in {city}"}, status.HTTP_200_OK)
        return Response({"message": "browse your current properties"}, status.HTTP_200_OK)
    def post(self, request):
        city = request.data.get("city")
        if not city:
            city = "your city"
        print(city)
        return Response({"message": f"you are uploading your property information in {city}"}, status.HTTP_200_OK)
    
