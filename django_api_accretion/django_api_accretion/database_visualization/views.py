from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
import requests

class DatabaseVisualizationView(APIView):
    def get(self, request):
        # address1 = request.GET.get('address1', '')
        # address2 = request.GET.get('address2', '')
        address1 = request.GET.get('address1','')
        address2 = request.GET.get('address2','')
        googleMapID = request.GET.get('googlemapid','')
        print("===addressInfo===", address1, "===address2===", address2)
        print("===googlemapid===", googleMapID)

        # if not address1 or not address2:
        #     return JsonResponse({'error': 'Missing address parameters'}, status=400)

        # Construct the API call to the third-party service
        api_url = f'https://api.attom.com/property/v3/{address1}'

        headers = {
            'apikey': 'your_attom_api_key',  # Replace with your actual API key
        }

        try:
            response = requests.get(api_url, headers=headers)
            response.raise_for_status()  # Raise an exception for HTTP errors
            data = response.json()
        except requests.RequestException as e:
            return JsonResponse({'error': str(e)}, status=500)

        return JsonResponse(data)
