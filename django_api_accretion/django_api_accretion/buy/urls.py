
# Import necessary libraries
from django.urls import path
from . import views

# Define URL patterns
urlpatterns = [
    path("", views.Buy.as_view(), name="buy"),
]
