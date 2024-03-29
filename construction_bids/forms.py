from django.db import models
from django.forms import ModelForm
from .models import ConstructionBid, Client, Task
from django.forms import inlineformset_factory

class ConstructionBidForm(ModelForm):
    class Meta:
        model = ConstructionBid
        fields = "__all__"

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = "__all__"    
 


