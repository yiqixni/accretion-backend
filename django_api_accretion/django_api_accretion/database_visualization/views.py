from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
import requests
from .models import PropertyData

API_key_Attoms = "596d978f1497eafd93fd11d382c11525" 

class DatabaseVisualizationView(APIView):
    def get(self, request):
        address1 = request.GET.get('address1','')
        address2 = request.GET.get('address2','')
        propertyID = request.GET.get('propertyid','')
        print("===addressInfo===", address1, "===address2===", address2)
        print("===propertyID===", propertyID)

        if not address1 or not address2:
            return JsonResponse({'error': 'Missing address parameters'}, status=400)

        try: #retrieve property data from Accretion Database
            propertyData = PropertyData.objects.get(propertyID = propertyID) 
            print("===property found in local database===")
            return JsonResponse(propertyData.data) 
        except: #retrieve property data from Attom through an API call 
            api_url = "https://api.gateway.attomdata.com/propertyapi/v1.0.0/saleshistory/basichistory" + f'?address1={address1}' + f'&address2={address2}'

            headers = {
                'apikey': API_key_Attoms,  # Replace with your actual API key
            }

            try:
                response = requests.get(api_url, headers=headers)
                response.raise_for_status()  # Raise an exception for HTTP errors
                data = response.json()
                try: # store the data into local database  
                    PropertyData.objects.create(
                        propertyID = data["status"]["attomId"], 
                        data = data 
                    )
                except Exception as e: 
                    print(e) 
                    
            except requests.RequestException as e:
                return JsonResponse({'error': str(e)}, status=500)

            return JsonResponse(data)
