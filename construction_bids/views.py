from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ConstructionBidForm, ClientFormSet, TaskFormSet
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
    construction_form = ConstructionBidForm
    # client_form = ClientForm    
    success_url = 'index-form-success/'

    ###########################################################
    # Get Method
    ###########################################################
    def get(self, request, *args, **kwargs):
        ''' 
        GET Response Method
        '''

        client_formset = ClientFormSet(prefix='client_set')
        task_formset = TaskFormSet(prefix='task_set')

        return TemplateResponse(request, self.template_name, { 
            'title': 'ModelFormClassCreateView Page',
            # 'page_id': 'model-form-class-id',
            # 'page_class': 'model-form-class-page',
            'h1_tag': 'This is the ModelFormClassCreateView Class Page Using ConstructionBidForm',
            'construction_form': self.construction_form(),
            'client_formset': client_formset,
            'task_formset': task_formset,

            # 'phone_formset': PhoneFormSet,
            # 'client_form': self.client_form(),
        })

    ###########################################################
    # Post Method
    ###########################################################
    def post(self, request, *args, **kwargs):
        ''' 
        POST Response Method
        '''

        construction_form = self.construction_form(request.POST)
        client_formset = ClientFormSet(request.POST, prefix='client_set')
        task_formset = TaskFormSet(request.POST, prefix='task_set')        

        if construction_form.is_valid() and client_formset.is_valid() and task_formset.is_valid():
            # If you need to manipulate fields in the parent form before saving
            # construction_form = construction_form.instance
            # construction_form = ConstructionBid(
            #   job_title = construction_form.instance.job_title,
            #   job_type = form.instance.job_type,
            #   estimate = form.instance.estimate,
            # )
            # construction_form.job_type = "TESTING"
            # construction_form.save()

            construction_bid = construction_form.save()

            # iterate through each form in the formset and save it
            client_instances = client_formset.save(commit=False)
            for client_instance in client_instances:
                client_instance.construction_bid = construction_bid
                client_instance.save()

            task_instances = task_formset.save(commit=False)
            for task_instance in task_instances:
                task_instance.client = construction_bid
                task_instance.save()
 
            return HttpResponseRedirect(self.success_url)
        else:
            return TemplateResponse(request, self.template_name, {
                'title': 'ModelFormClassCreateView Page - Please Correct The Errors Below',
                'page_id': 'model-form-class-id',
                'page_class': 'model-form-class-page errors-found',
                'h1_tag': 'This is the ModelFormClassCreateView Page Using ConstructionBidform<br />' \
                    '<small class="error-msg">Errors Found</small>',
                'construction_form': construction_form,
                'client_formset': client_formset,
                'task_formset': task_formset,                
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