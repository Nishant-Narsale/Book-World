from django.urls import path, include
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index , name="index"),
    path('cart/', views.cart , name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('profile/', views.profile, name="profile"),
    path('category/<str:category_name>', views.category, name="category"),
    path('about/',views.about, name="about"),
    path('updateItem/', views.updateItem, name="updateItem"),
    path('sell_book/', views.sellItem, name="sellItem")
] 