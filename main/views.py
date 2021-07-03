from django.shortcuts import render
from django.contrib import messages
from django.http import JsonResponse
import json
from .models import *
# Create your views here.

def index(request):
    
    books = Products.objects.all()

    if request.user.is_authenticated:
        user_is_authenticated = True
        customer = request.user.customer
        order = Order.objects.get(customer=customer)

    else:
        books = Products.objects.all()
        user_is_authenticated = False
        order = []

    context = {
        'books':books,
        'user_is_authenticated':user_is_authenticated,
        'order':order
        }
    return render(request, 'index.html', context)

def cart(request):
    if request.user.is_authenticated :
        user_is_authenticated = True
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,complete=False)
        order_items = order.orderitem_set.all()

    else:
        user_is_authenticated = False
        order = []
        order_items = []

    context = {
        "order_items":order_items,
        'user_is_authenticated':user_is_authenticated,
        "order":order
        }
    return render(request, 'cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        user_is_authenticated = True
        customer = request.user.customer
        order = Order.objects.get(customer=customer)
        order_items = order.orderitem_set.all()

    else:
        user_is_authenticated = False
        order = []
        order_items = []
    
    context = {
        'user_is_authenticated':user_is_authenticated,
        'order_items':order_items,
        'order':order
    }
    return render(request, 'checkout.html', context)

def profile(request):
    if request.user.is_authenticated:
        user_is_authenticated = True
        user = request.user
        customer = request.user.customer
        order = Order.objects.get(customer=customer)

    else:
        user = {'username':'Guest User','email':'guest@gmail.com',}
        user_is_authenticated = False
        order = []

    context = {
        'user_is_authenticated':user_is_authenticated,
        'user':user,
        'order':order
    }
    return render(request, 'profile.html', context)

def about(request):
    about_page = True
    if request.user.is_authenticated:
        user_is_authenticated = True
        customer = request.user.customer

    else:
        user_is_authenticated = False
        
    context = {
        'user_is_authenticated':user_is_authenticated,
        'about_page':about_page,
    }
    return render(request, 'about.html', context)

def category(request, category_name):
    category_page = True
    
    books = Products.objects.filter(category=category_name)
    if request.user.is_authenticated:
        user_is_authenticated = True
        customer = request.user.customer
        order = Order.objects.get(customer=customer)

    else:
        user_is_authenticated = False
        order = []

    context = {
        'user_is_authenticated':user_is_authenticated,
        'category_page':category_page,
        'category_name':category_name,
        'books':books,
        'order':order
        }
    return render(request, 'layout_categories.html' ,context)

def updateItem(request):
    
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Product Id:',productId)
    print('Action:',action)
    product = Products.objects.get(id=productId)
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer)
    try:
        orderItem = OrderItem.objects.get(order=order, product=product)
    except:
        orderItem = OrderItem.objects.create(order=order, product=product, quantity=0)

    if action=='add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action=='remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if action=='removeItem':
        orderItem.delete()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse("Item is added", safe=False)

def sellItem(request):
    sell_page = True
    context = {
        'sell_page':sell_page
    }
    return render(request, 'sell.html', context) 