from collections.abc import Iterable
from django.db import models
from account.models import User
from django.contrib.auth import get_user_model
from slugify import slugify


User = get_user_model()


class Customer(models.Model):
    customer = models.OneToOneField(User, on_delete=models.CASCADE)
    name  = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)


    def __str__(self):
        return self.name







class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(null=True, blank=True)

    class Meta:
        ordering = ('-name',)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f"/{self.slug}/"
    
    def save(self,*args, **kwargs):
        self.slug = slugify(self.name)
        return super(Category, self).save(*args, **kwargs)
    
    
    




class Product(models.Model):
    product_name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE )
    product_img = models.ImageField(upload_to='product/images',default="")
    product_discription = models.CharField(max_length=1000)
    product_price  = models.DecimalField(max_digits=7, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)
    product_slug = models.SlugField()
    product_quantity = models.PositiveIntegerField()
        
    def __str__(self):
        return self.product_name
    
    def get_absolute_url(self):
        return f"/{self.category.slug}/{self.product_slug}"
    
    def get_product_img(self):
        if self.product_img:
            return "http://127.0.0.1:8000"+ self.product_img
        return " "
    @property
    def get_image(self):
        try:
            url = self.product_img.url
        except:
            url = ""
            return url






class Address(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    pincode = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    created_at =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"/{self.name}/address : /{self.address}/"


# # cart


# class cart(models.Model):











class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    products = models.ManyToManyField(Product, through='OrderItem')
    address = models.ForeignKey(Address,  on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)
    status = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True) 

    
    def __str__(self):
        return f"Order #{self.pk} by {self.customer.customer.first_name}"
    

    @property
    def total_price(self):
        total = self.product.product_price * self.quantity
        return total

    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    
    def __str__(self):
        return f'{self.quantity} x {self.product.name}'

class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Payment for Order #{self.order.pk}'


    

    




