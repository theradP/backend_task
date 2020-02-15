from django.db import models
from datetime import datetime
# Create your models here.
class Device(models.Model):
    name = models.CharField(max_length = 50, primary_key= True)
    date = models.DateTimeField(default = datetime.now)
    device_ip = models.URLField()
    class Meta:
        db_table = 'devices'

class Operations(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    task = models.CharField(max_length = 200)
    class Meta:
        db_table = 'operations'

