from django.urls import path
from . import views 

urlpatterns = [
    path("", views.SellerUpload.as_view(), name="seller-upload"),
]


# # use class-based APIViews
# from . import views_APIView 
# urlpatterns = [
#     path("", views_APIView.Sell.as_view(), name="sell"),
# ]

## use function-based views
# from . import views_apiview_decorator
# urlpatterns = [
#     path("", views_apiview_decorator.sell, name="sell"),
# ]