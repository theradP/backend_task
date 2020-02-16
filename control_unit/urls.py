from django.contrib import admin
from django.urls import path, include
from .views import HomeController, DeviceController

urlpatterns = [

    path('list_devices/', DeviceController.as_view()),
    path('add_device/', HomeController.as_view()),
    path('remove_device/', HomeController.as_view()),
    path('do_task/', DeviceController.as_view()),
]