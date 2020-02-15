from django.contrib import admin
from django.urls import path, include, url
from .views import HomeController, DeviceController

urlpatterns = [

    url('/list_devices/', DeviceController.as_view()),
    url('/add_device/', HomeController.as_view()),
    url('/remove_device/', HomeController.as_view()),
    url('/do_task/', DeviceController.as_view()),
]