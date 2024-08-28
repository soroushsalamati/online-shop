from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name





class Product(models.Model):  
        name = models.CharField(  
            max_length=50,  
            verbose_name="Product Name",  
            help_text="Enter the name of the product."  
        )  
        description = models.TextField(  
            help_text="Provide a detailed description of the product."  
        )  
        price = models.FloatField(  
            help_text="Enter the original price of the product."  
        )  
        off_price = models.FloatField(  
            default=None,  
            help_text="Enter the discounted price of the product, if applicable."  
        )  
        category = models.ForeignKey(Category, on_delete=models.CASCADE, help_text="Select category for the order.")

        def __str__(self) -> str:  
            return self.name  
        



class Customer(models.Model):  
        username = models.CharField(  
            max_length=20,  
            help_text="Enter the username of the customer."  
        )  
        address = models.TextField(  
            help_text="Enter the address of the customer."  
        )  
        post_id = models.CharField(  
            max_length=50,  
            verbose_name="Postal ID",  
            help_text="Enter the postal ID of the customer."  
        )  

        def __str__(self) -> str:  
            return self.username  


class Order(models.Model):  
        cart = models.ManyToManyField(Product, help_text="Select products for the order.")  
        date = models.DateField(  
            help_text="Select the date of the order."  
        )  
        order_id = models.CharField(  
            max_length=50,  
            verbose_name="Order ID",  
            help_text="Enter a unique identifier for the order."  
        )  
        costumer = models.ForeignKey(Customer, on_delete=models.CASCADE, help_text="Select the customer for this order.")  
        
        def __str__(self) -> str:  
            return self.order_id  
    

class Factor(models.Model):  
        order = models.ForeignKey(Order, on_delete=models.CASCADE, help_text="Select the order associated with this factor.")  
        total_price = models.FloatField(  
            help_text="Enter the total price for the order."  
        )  