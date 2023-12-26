from django.contrib import admin
from . models import PickupRequest,CustomerAddress,CustomerDetails

# Register your models here.

admin.site.register(PickupRequest)
admin.site.register(CustomerAddress)
admin.site.register(CustomerDetails)