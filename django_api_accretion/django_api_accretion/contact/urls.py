from django.urls import path
from . import views

urlpatterns = [
    path("", views.ContactUs, name="contact-us"), 
]