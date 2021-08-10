from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.core.validators import RegexValidator

# Create your models here.
class Region(models.Model):
    region_name= models.CharField(max_length=255, db_index=True)

    def __str__(self):
        return self.region_name

class Zone(models.Model):
    zone_name= models.CharField(max_length=255, db_index=True)

    def __str__(self):
        return self.zone_name

class Woreda(models.Model):
    woreda_name= models.CharField(max_length=255, db_index=True)

    def __str__(self):
        return self.woreda_name

class Basin(models.Model):
    basin_name= models.CharField(max_length=255, db_index=True)

    def __str__(self):
        return self.basin_name

class MSC(models.Model):
    msc_name= models.CharField(max_length=255, db_index=True)

    def __str__(self):
        return self.msc_name

class StationType(models.Model):
    station_type = models.CharField(max_length=255, db_index=True)
    description = models.TextField(max_length=500, db_index=True)

    def __str__(self):
        return self.station_type

class Station(models.Model):
    station_id = models.CharField(max_length=255, db_index=True)
    begin_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField()
    name = models.CharField(max_length=255, db_index=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE)
    woreda = models.ForeignKey(Woreda, on_delete=models.CASCADE)
    basin = models.ForeignKey(Basin, on_delete=models.CASCADE)
    station_type = models.ForeignKey(StationType, on_delete=models.CASCADE)
    msc = models.ForeignKey(MSC, on_delete=models.CASCADE)
    geography_1 = models.FloatField(max_length=255, db_index=True)
    longitude = models.CharField(max_length=255, db_index=True)
    geography_2 = models.FloatField(max_length=255, db_index=True)
    latitude = models.CharField(max_length=255, db_index=True)
    elevation = models.FloatField(max_length=255, db_index=True)
    note = models.TextField(max_length=500, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('station:station-list')
