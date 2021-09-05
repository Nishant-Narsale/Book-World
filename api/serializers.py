from django.db.models import fields
from rest_framework import serializers
from main.models import *


class ProductsSerializer(serializers.ModelSerializer):
    class Meta():
        model = Products
        exclude = ['image']