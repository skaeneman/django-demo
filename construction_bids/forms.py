from django.db import models
from django.forms import ModelForm
from .models import ConstructionBid

class ConstructionBidForm(ModelForm):
    class Meta:
        model = ConstructionBid
        fields = "__all__"