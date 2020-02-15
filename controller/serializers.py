from .models import Device
from rest_framework import serializers


class Listserializers(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ['name', 'device_ip']