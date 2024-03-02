from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register("car", views.CarViewSet, basename="car")
app_name = "app_api"

urlpatterns = [path("", views.home, name="home"), path("car/", include(router.urls))]
