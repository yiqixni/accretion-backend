# from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated 
from rest_framework.decorators import permission_classes
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle

# Create your views here.
# @permission_classes([IsAuthenticated])
class Buy(APIView):
    throttle_classes = [UserRateThrottle, AnonRateThrottle] 
    def get(self, request):
        if request.user.groups.filter(name="Manager").exists():
            return Response({"message": "entering Manager's buy page"}) 
        elif request.user.groups.filter(name="Customer").exists():
            return Response({"message": "entering Customer's buy page"})
        else: 
            return Response({"message": "entering anon user's buy page"})