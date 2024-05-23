from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView 
from rest_framework import status 

# from .models import DeedRecords 
from .serializers import DeedRecordsSerializer
from .tests import testsDell 


# Create your views here. 
class DeedRecrodsAPIView (RetrieveAPIView): 

    def retrieve (self, request, *args, **kwargs): 
        # get the address from frontend client 
        state = request.query_params.get('state')
        county = request.query_params.get('county') 
        town = request.query_params.get('town') 
        street_name = request.query_params.get('street_name')
        street_number = request.query_params.get('street_number')                       
        # run testDell.py to retrieve the deed information form HTML
        deed_record_demo = testsDell()             
        # serialize the json data to the database 
        serializer = DeedRecordsSerializer(data=deed_record_demo, many=True)
        serializer.is_valid(raise_exception=True)
        # return the serialized data back to the frontend client 
        return Response(serializer.data, status = status.HTTP_200_OK) 
        