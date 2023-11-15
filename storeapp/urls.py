from django.urls import path 
from storeapp.views import Productlistview



urlpatterns = [
    path('products/',Productlistview.as_view(), name="products"),
]

