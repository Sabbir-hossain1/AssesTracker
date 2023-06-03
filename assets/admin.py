from django.contrib import admin

from assets.models import Device, DeviceAssignment

# Register your models here.
admin.site.register(Device)
admin.site.register(DeviceAssignment)
