from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import ConstructionBid, Client
from .forms import ConstructionBidForm
from django.contrib import messages
from django.template.response import TemplateResponse
from django.views.generic.edit import (
    FormView,
    CreateView,
    UpdateView,
)
# Create your views here.

class ConstructionBidClassCreateView(CreateView):

    template_name = 'index.html'
    form_class = ConstructionBidForm
    success_url = 'index-form-success/'

    ###########################################################
    # Get Method
    ###########################################################
    def get(self, request, *args, **kwargs):
        '''
        GET Response Method
        '''
 
        return TemplateResponse(request, self.template_name, { 
            'title': 'ModelFormClassCreateView Page',
            # 'page_id': 'model-form-class-id',
            # 'page_class': 'model-form-class-page',
            'h1_tag': 'This is the ModelFormClassCreateView Class Page Using ConstructionBidForm',
            'form': self.form_class(),
        })

    ###########################################################
    # Post Method
    ###########################################################
    def post(self, request, *args, **kwargs):
        '''
        POST Response Method
        '''
        #return redirect(self.success_url)
        form = self.form_class(request.POST)

        if form.is_valid():
            bid_form = form.instance

            # If you need to manipulate fields individually
            # bid_form = ConstructionBid(
            #   job_title = form.instance.job_title,
            #   job_type = form.instance.job_type,
            #   estimate = form.instance.estimate,
            # )
            # bid_form.job_type = "TESTING"
            # bid_form.save()

            return HttpResponseRedirect(self.success_url)
        else:
            return TemplateResponse(request, self.template_name, {
                'title': 'ModelFormClassCreateView Page - Please Correct The Errors Below',
                # 'page_id': 'model-form-class-id',
                # 'page_class': 'model-form-class-page errors-found',
                'h1_tag': 'This is the ModelFormClassCreateView Page Using ConstructionBidform<br />' \
                    '<small class="error-msg">Errors Found</small>',
                'form': form,
            })

    def form_valid(self, form):
        '''
        This method is called when valid form data has been POSTed.
        It should return an HttpResponse.
        '''

        # Perform Additional Actions, such as sending an email or custom business logic
        # validation checking.
        #form.send_email()
        return super().form_valid(form)