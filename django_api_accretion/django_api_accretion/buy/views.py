from rest_framework.generics import ListAPIView
from sell.models import PropertyInfo
from sell.serializers import PropertyInfoSerializer

class Buy(ListAPIView): 
    queryset = PropertyInfo.objects.all() 
    serializer_class = PropertyInfoSerializer 
    
    def get_queryset(self):
        id = self.request.query_params.get("id", None) 
        queryset = PropertyInfo.objects.all() 
        if id: 
            queryset = queryset.filter(id=id) 
        
        return queryset 