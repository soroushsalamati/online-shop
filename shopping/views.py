from django.http.response import HttpResponse , JsonResponse
from shopping.models import Customer , Order , Product ,Factor, Category
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import render


def product_list(request):
    products = Product.objects.all()
    my_product_list = []
    for item in products:
        product_dictionary = {
            "name" : item.name,
            "description" : item.description,
            "price" : item,
            "category" : item.category.name
        }
        my_product_list.append(product_dictionary)
    return JsonResponse(my_product_list, safe=False)