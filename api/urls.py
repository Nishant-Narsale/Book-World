from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('',views.ApiOverview,name='apioverview'),
    path('products/',views.ProductsView,name='products'),
    path('create-product/',views.CreateProduct,name='create-product'),
    path('update-product/<str:id>/',views.UpdateProduct,name='update-product'),
    path('delete-product/<str:id>/',views.DeleteProduct,name='delete-product'),
]