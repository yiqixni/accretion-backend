from rest_framework.response import Response 
from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser 
from .models import PropertyInfo 
from .serializers import PropertyInfoSerializer   
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes 


class SellerUpload(generics.CreateAPIView, generics.ListAPIView):
    permission_classes = [IsAuthenticated] 
    queryset = PropertyInfo.objects.all()
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = PropertyInfoSerializer 
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user,
                        username=self.request.user.username)
    
    def get_queryset(self): 
        return PropertyInfo.objects.filter(user=self.request.user)
    
    ## create a GET method to return username from JWT token
    # def get(self, request):
    #     return Response({"username": request.user.username})
    
    # # override GET with custom method 
    # def get(self,request): 
    #     queryset = PropertyInfo.objects.all() 
    #     serializer = PropertyInfoSerializer(queryset, many=True) 
    #     return Response(serializer.data)
    
    # def post(self, request, *args, **kwargs):
    #     request_data = request.data  
    #     return Response(request_data) 