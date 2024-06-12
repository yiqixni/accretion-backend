from django.urls import path
from .views import CreateTagsView 

urlpatterns = [
    path('', CreateTagsView.as_view(), name='create-tags'), 
]