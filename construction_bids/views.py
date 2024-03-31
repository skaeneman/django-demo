from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import ConstructionBid, Client
from .forms import ConstructionBidForm, ClientFormSet, TaskFormSet
from django.contrib import messages
from django.template.response import TemplateResponse
from django.views.generic.edit import (
    FormView,
    CreateView,
    UpdateView,
)
from django.forms import inlineformset_factory


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

        return TemplateResponse(request, self.template_name, { 
            'title': 'ModelFormClassCreateView Page',
            # 'page_id': 'model-form-class-id',
            # 'page_class': 'model-form-class-page',
            'h1_tag': 'This is the ModelFormClassCreateView Class Page Using ConstructionBidForm',
            'construction_form': self.construction_form(),
            'client_formset': ClientFormSet(prefix='client_set'),
            'task_formset': TaskFormSet(prefix='task_set'),

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
        #return redirect(self.success_url)
        construction_form = self.construction_form(request.POST)

        # client formset, get the instance of the construction form
        client_formset = ClientFormSet(request.POST, instance=construction_form.instance)

        # task formset, get the instance of the construction form
        task_formset = TaskFormSet(request.POST, instance=construction_form.instance)


        if construction_form.is_valid() and client_formset.is_valid() and task_formset.is_valid():
            construction_form = construction_form.instance

            # print(client_formset)

            # If you need to manipulate fields individually
            # construction_form = ConstructionBid(
            #   job_title = construction_form.instance.job_title,
            #   job_type = form.instance.job_type,
            #   estimate = form.instance.estimate,
            # )
            # construction_form.job_type = "TESTING"
            # construction_form.save()


            # Create, but don't save the bid instance.
            # construction = construction_form.save(commit=False)
            
            # Save the bid instance
            parent = construction_form.save()

            # instances = client_formset.save(commit=False)
            # for obj in client_formset.deleted_objects:
            #   obj.delete()


            # loop through the formset and save each form
            for client_form in client_formset:
                client_form.construction_bid = parent
                client_form.save()
            
            # loop through the formset and save each form
            for task_form in task_formset:
                task_form.construction_bid = parent
                task_form.save() 


            return HttpResponseRedirect(self.success_url)
        else:
            return TemplateResponse(request, self.template_name, {
                'title': 'ModelFormClassCreateView Page - Please Correct The Errors Below',
                'page_id': 'model-form-class-id',
                'page_class': 'model-form-class-page errors-found',
                'h1_tag': 'This is the ModelFormClassCreateView Page Using ConstructionBidform<br />' \
                    '<small class="error-msg">Errors Found</small>',
                'construction_form': construction_form,
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