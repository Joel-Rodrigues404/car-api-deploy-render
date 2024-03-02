# from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import CarSerializer
from .models import Car
from django.http import HttpResponse

# Create your views here.


class CarViewSet(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

def home(request):
    return HttpResponse("deu massa")