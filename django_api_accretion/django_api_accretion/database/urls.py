from django.urls import path
from .views import DeedRecrodsAPIView

urlpatterns = [
    path('', DeedRecrodsAPIView.as_view(), name='deed-records'),
]
