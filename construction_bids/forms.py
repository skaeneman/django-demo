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
 
# client formset
ClientFormSet = inlineformset_factory(ConstructionBid, Client, fields=("first_name","last_name",), extra=0, can_delete_extra=True)

#task formset
TaskFormSet = inlineformset_factory(ConstructionBid, Task, form=TaskForm, extra=1, can_delete_extra=True)

