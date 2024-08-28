from django.urls import path
from shopping.views import product_list


urlpatterns = [
    path('product_list/' , product_list),
]