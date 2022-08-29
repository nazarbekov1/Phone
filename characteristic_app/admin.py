from django.contrib import admin
from .models import Display, NetworkSupport, Camera, ComputingResources, Battery,\
    SecureAuthentication, DisplayAndBody, WaterAndDustProtection, AudiAndVideo,  DimensionsAndWeight, ContentsOfDelivery


admin.site.register(Display)
admin.site.register(NetworkSupport)
admin.site.register(Camera)
admin.site.register(ComputingResources)
admin.site.register(Battery)
admin.site.register(SecureAuthentication)
admin.site.register(DisplayAndBody)
admin.site.register(WaterAndDustProtection)
admin.site.register(AudiAndVideo)
admin.site.register(DimensionsAndWeight)
admin.site.register(ContentsOfDelivery)

