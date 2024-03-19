from django.contrib import admin
from .models import ConstructionBid, Client

# Register your models here.
admin.site.register(ConstructionBid)
admin.site.register(Client)