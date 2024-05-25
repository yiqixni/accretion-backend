from django.urls import path
from .views import DatabaseVisualizationView
from .views import UploadPNGView 

urlpatterns = [
    path('get-data/', DatabaseVisualizationView.as_view(), name='database-visualization'),
    path('post-png/', UploadPNGView.as_view(), name='upload-png'), 
]