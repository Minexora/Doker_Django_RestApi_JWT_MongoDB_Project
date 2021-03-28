from rest_framework import serializers
from api.models import *
from django.shortcuts import get_object_or_404


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
