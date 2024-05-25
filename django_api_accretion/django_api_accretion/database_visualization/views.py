from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
import requests
from .models import PropertyData
from .serializers import PropertyDataSerializer 

API_key_Attoms = "596d978f1497eafd93fd11d382c11525" 

class DatabaseVisualizationView(APIView):
    def get(self, request):
        address1 = request.GET.get('address1','')
        address2 = request.GET.get('address2','')
        propertyID = request.GET.get('propertyid','')        

        if not address1 or not address2:
            return JsonResponse({'error': 'Missing address parameters'}, status=400)

        query_string = f'address1={address1}&address2={address2}'                
        
        try: #retrieve property data from Accretion Database by property ID
            propertyData = PropertyData.objects.get(propertyID = propertyID) 
            print("===property data found in local database by property ID ===")
            serializer = PropertyDataSerializer(propertyData) 
            
            return JsonResponse(serializer.data['data']) 
        
        except Exception as e:
            print("===data not found by property id===")
            print(e)
            
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

        try:
            response = requests.get(api_url, headers=headers)
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
        
