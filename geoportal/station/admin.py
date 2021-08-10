from django.contrib import admin
from station.models import StationType, Region, Zone, Woreda, Basin, MSC

# Register your models here.
admin.site.register(StationType)
admin.site.register(Region)
admin.site.register(Zone)
admin.site.register(Woreda)
admin.site.register(Basin)
admin.site.register(MSC)
