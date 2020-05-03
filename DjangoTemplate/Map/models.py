from django.db import models


class AMapInfo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,default='name')
    lng = models.FloatField(max_length=16,blank=False)
    lat = models.FloatField(max_length=16,blank=False)
    is_open = models.BooleanField(default=False)
    open_time = models.CharField(max_length=255)
    note = models.CharField(max_length=16)
