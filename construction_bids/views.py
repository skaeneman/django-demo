from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ConstructionBid, Client
from .forms import ConstructionBidForm
from django.contrib import messages
from django.template import loader

# Create your views here.

def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())




# Create your views here.
# def index(request):
# 	if request.method == "POST":
# 		construction_form = ConstructionBidForm(request.POST)
# 		if construction_form.is_valid():
# 			construction_form.save()
# 			messages.success(request, ('Your bid was successfully added!'))
# 		else:
# 			messages.error(request, 'Error saving form')
		
		
# 		return redirect("construction_bids:index")
# 	construction_form = ConstructionBidForm()
# 	bids = ConstructionBid.objects.all()
# 	return render(request=request, template_name="construction_bids/index.html", context={'construction_form':construction_form, 'bids':bids})