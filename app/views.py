# from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import CarSerializer
from .models import Car

# Create your views here.


class CarViewSet(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
