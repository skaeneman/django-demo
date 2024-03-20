from django.db import models
from django.forms import ModelForm
from .models import ConstructionBid, Client

class ConstructionBidForm(ModelForm):
    class Meta:
        model = ConstructionBid
        fields = "__all__"

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = "__all__"        