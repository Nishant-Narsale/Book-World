from django.db import models
from django.contrib.auth.models import User

# Create your models here.

category_choice = {
    ('F.Y.Engineering','F.Y.Engineering'),
    ('S.Y.Engineering','S.Y.Engineering'),
    ('Horror','Horror'),
    ('Comic','Comic'),
    ('Science Fiction','Science Fiction'),
    ('other','other')
}

class Products(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    price = models.FloatField(blank=True, null=True)
    image = models.ImageField(null=True,blank=True)
    category = models.CharField(max_length=120, default='other', choices=category_choice)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            return self.image.url
        except:
            return ''

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=120, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.user.username



class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE, null=True, blank=True)
    date_ordered = models.DateField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.IntegerField(null=True)

    @property
    def total_cart_items(self):
        order_items = self.orderitem_set.all()
        total = 0
        for item in order_items:
            total += item.quantity

        return total

    @property
    def total_cart_price(self):
        order_items = self.orderitem_set.all()
        total = 0
        for item in order_items:
            total += item.total_price

        return total

class OrderItem(models.Model):
    product = models.ForeignKey(Products, on_delete=models.SET_NULL , null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    date_added = models.DateField(auto_now_add=True)

    @property
    def total_price(self):
        return self.product.price * self.quantity

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL , null=True, blank=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    zipcode = models.CharField(max_length=200, null=False)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.address
