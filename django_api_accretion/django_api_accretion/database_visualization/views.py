import os 
import requests

from dotenv import load_dotenv 

from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response

from .models import PropertyData
from .serializers import PropertyDataSerializer, PropertyDataForView 

# Get API from the .env
load_dotenv()
API_key_Attoms = os.getenv('API_KEY_ATTOMS')

# Get proxy config
proxy_host      = os.getenv('PROXY_HOST')
proxy_port      = os.getenv('PROXY_PORT')
proxy_user      = os.getenv('PROXY_USER')
proxy_password  = os.getenv('PROXY_PASSWORD')
# Create the proxy URL
proxy_url = f'http://{proxy_user}:{proxy_password}@{proxy_host}:{proxy_port}'



# Handle search request for property: returns the json property data 
class DatabaseVisualizationView(APIView):
    def get(self, request):
        address1 = request.GET.get('address1','')
        address2 = request.GET.get('address2','')
        propertyID = request.GET.get('propertyid','')                              
        
        try: #retrieve property data from Accretion Database by property ID
            propertyData = PropertyData.objects.get(propertyID = propertyID) 
            print("===property data found in local database by property ID ===")
            serializer = PropertyDataSerializer(propertyData) 
            
            return JsonResponse(serializer.data['data']) 
        
        except Exception as e:
            print("===data not found by property id===")
            print(e)
            
        if not address1 or not address2:
            return JsonResponse({'error': 'Missing address parameters'}, status=400)

        query_string = f'address1={address1}&address2={address2}'  
            
        try: #retrieve property data from Accretion Database by query string
            propertyData = PropertyData.objects.get(query_string = query_string) 
            print("===property data found in local database by query string===")
            serializer = PropertyDataSerializer(propertyData)             
            
            return JsonResponse(serializer.data['data']) 
        
        except Exception as e:
            print("===data not found by query string===")
            print(e)
        
        # except: #retrieve property data from Attom through an API call 
            
        print("===API call to Attom===")
        
        api_url = "https://api.gateway.attomdata.com/propertyapi/v1.0.0/saleshistory/basichistory?" + query_string 
        headers = {
            'apikey': API_key_Attoms,  # Replace with your actual API key
        }
        proxies = {
            'http' : proxy_url,
            'https': proxy_url,
            }

        try:
            response = requests.get(api_url, headers=headers, proxies=proxies)
            response.raise_for_status()  # Raise an exception for HTTP errors
            data = response.json()                
            try: # store the data into local database                      
                property_data_obj, created = PropertyData.objects.update_or_create(
                    propertyID=data["status"]["attomId"],
                    defaults={'data': data, 'query_string': query_string} 
                )
                if created:
                    print("===New property data stored in local database===")
                else:
                    print("===Property data updated in local database===")
                    
                serializer = PropertyDataSerializer(property_data_obj) 
                
                return JsonResponse(serializer.data['data']) 
                
            except Exception as e: 
                print(e) 
                
        except requests.RequestException as e:
            return JsonResponse({'error': str(e)}, status=500)
        
# Handle image preview post request returns image preview link 
class UploadPNGView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        propertyID = request.data.get('propertyID')
        image = request.data.get('image')                

        if not propertyID or not image:
            return Response({"error": "propertyID and image are required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            property_data = PropertyData.objects.get(propertyID=propertyID)
        except PropertyData.DoesNotExist:
            return Response({"error": "PropertyData not found"}, status=status.HTTP_404_NOT_FOUND)

        # Save the image to the static directory
        image_path = os.path.join(settings.MEDIA_ROOT, 'database_visualization', f"{propertyID}.png")
        os.makedirs(os.path.dirname(image_path), exist_ok=True)

        with open(image_path, 'wb+') as destination:  # Open the file for writing in binary mode
            for chunk in image.chunks(): # Read the uploaded file in chunks
                destination.write(chunk) # Write each chunk to the destination file

        # Update the property data with the image link
        image_url = f"{settings.MEDIA_URL}database_visualization/{propertyID}.png"
        property_data.imageLink = image_url
        property_data.save()
        # Create a full image URL back to the frontend 
        full_image_url = request.build_absolute_uri(image_url)

        return Response({"imageLink": full_image_url}, status=status.HTTP_200_OK)
    
# Handle view get request returns the json property data and preview image 
class GetPropertyDataImageLinkView(APIView): 
    def get(self, request): 
        propertyID = request.GET.get('propertyid', '') 
        print("=== get property data and image link === propertyID=", propertyID)
        
        try: #retrieve property data from Accretion Database by property ID
            propertyData = PropertyData.objects.get(propertyID = propertyID) 
            print("===property data found in local database by property ID ===")
            serializer = PropertyDataForView(propertyData, context={'request': request}) #use context to give imageLink the full URL
            
            return JsonResponse(serializer.data) 
        
        except requests.RequestException as e:
            return JsonResponse({'error': str(e)}, status=500)