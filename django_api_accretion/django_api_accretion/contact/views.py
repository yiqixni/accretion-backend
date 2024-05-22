# from django.shortcuts import render
from rest_framework.response import Response 
from rest_framework import status 
from rest_framework.decorators import api_view 
from .serializers import ContactInfoSerializer  
from django.core.mail import send_mail 


# Create your views here.
@api_view(["GET", "POST"]) 
def ContactUs(request):
    if request.method == "GET":
        return Response({"message": "Call us at 617-233-2293, or email us at support@accretion.life"
                         }, status=status.HTTP_200_OK)
    
    if request.method == "POST":
        serialized_contact_info = ContactInfoSerializer(data=request.data)
        serialized_contact_info.is_valid(raise_exception=True)  
        serialized_contact_info.save()  
        clientName = serialized_contact_info.data.get("name") 
        
        email_subject = "Thanks for Contacting Accretion" 
        email_message = f"Hi {clientName}, your message received! Our customer support will contact you soon" 
        email_from = "yiqinix@gmail.com" 
        email_to = ["support@accretion.life"]
        
        send_mail(subject=email_subject, 
                  message = email_message, 
                  from_email=email_from,
                  recipient_list=email_to, 
                  fail_silently=False
                  )
        
        
        return Response(
            {"message": f"Hi {clientName}, your message received! Our customer support will contact you soon"}, 
            status=status.HTTP_200_OK)