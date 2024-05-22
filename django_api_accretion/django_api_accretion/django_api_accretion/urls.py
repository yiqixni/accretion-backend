"""
URL configuration for django_api_accretion project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static 
from django.conf import settings 
## DRF token-based and JWT authentication
# from rest_framework.authtoken.views import obtain_auth_token 
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenBlacklistView

urlpatterns = [
    path("admin/", admin.site.urls), 
    path("api/buy/", include("buy.urls")),
    path("api/sell/", include("sell.urls")), 
    path("api/contact-us/", include("contact.urls")),
    path("api/database/", include("database.urls")),
    ## Django debug toolbar
    path("__debug__/", include("debug_toolbar.urls")),
    ## Djoser library 
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")), # for JWT authentication
    # path("auth/", include("djoser.urls.authtoken")), # for DRF token authentication
    ## DRF built in authentication 
    # path("api/api-auth/", obtain_auth_token),
    ## JWT authentication 
    # path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),    
    # path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),   
    # path("api/token/blacklist/", TokenBlacklistView.as_view(), name="token_blacklist"), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
