from django.contrib import admin
from .models import ConstructionBid, Client, Task

# Register your models here.
admin.site.register(ConstructionBid)
admin.site.register(Client)
admin.site.register(Task)  
