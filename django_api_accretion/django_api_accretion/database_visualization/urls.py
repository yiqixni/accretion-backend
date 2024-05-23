from django.urls import path
from .views import DatabaseVisualizationView

urlpatterns = [
    path('', DatabaseVisualizationView.as_view(), name='database-visualization'),
]