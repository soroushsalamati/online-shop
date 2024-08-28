from django.contrib.admin import register , ModelAdmin
from shopping.models import Order , Product , Customer


@register(Order)  
class OrderAdmin(ModelAdmin):  
    list_display = [  
        'date',  
        'order_id',  
        'costumer',  
    ]  
    search_fields = [  
        'order_id',  
        'costumer__username',  
    ]  
    list_filter = [  
        'date',  
        'costumer',  
    ]  

@register(Product)  
class ProductAdmin(ModelAdmin):  
    list_display = [  
        'name',  
        'price',  
        'off_price',  
    ]  
    search_fields = [  
        'name',  
        'description',  
    ]  
    list_filter = [  
        'price',  
        'off_price',  
    ]  

@register(Customer)  
class CustomerAdmin(ModelAdmin):  
    list_display = [  
        'username',  
        'address',  
        'post_id',  
    ]  
    search_fields = [  
        'username',  
        'address',  
    ]  