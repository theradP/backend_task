from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Device, Operations
from datetime import datetime
from .serializers import Listserializers
# Create your views here.
class HomeController(APIView):
    def post(self,request):
        #add new device
        name = request.data.get('name', None)
        ip = request.data.get('ip', None)
        try:
            obj = Device()
            obj.name = name
            obj.device_ip = ip
            obj.save()
            return Response('device saved', status=200)
        except Exception as e:
            output = "Error in recieving device configuration"
            return Response(output, status=400)

    def delete(self,request):
        #remove device
        name = request.data.get('name', None)
        if name:
            Device.objects.filter(name=name).delete()
            return Response("device removed", status=200)
        else:
            return Response('name required', status=400)

class DeviceController(APIView):
    def post(self,request):
        #do_task
        start = datetime.now
        device_name = request.data.get('name', None)
        device = Device.objects.filter(name=device_name)
        task = request.data.get('task', None)
        #call task api or function
        end = datetime.now
        obj = Operations(device=device, start_time=start, end_time=end, task=task)
        obj.save()
        return Response("task completed", status=200)

    def get(self):
        #list add devices
        devices = Device.objects.all()
        data = Listserializers(devices)
        return Response(data, status=200)
