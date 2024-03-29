from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import ConstructionBid, Client, Task
from .forms import ConstructionBidForm, TaskForm
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

        # client formset
        ClientFormSet = inlineformset_factory(ConstructionBid, Client, fields=("first_name","last_name",), extra=1, can_delete_extra=True)
        #task formset
        TaskFormSet = inlineformset_factory(ConstructionBid, Task, form=TaskForm, extra=1, can_delete_extra=True)

        return TemplateResponse(request, self.template_name, { 
            'title': 'ModelFormClassCreateView Page',
            # 'page_id': 'model-form-class-id',
            # 'page_class': 'model-form-class-page',
            'h1_tag': 'This is the ModelFormClassCreateView Class Page Using ConstructionBidForm',
            'construction_form': self.construction_form(prefix='construction_bid'),
            'client_formset': ClientFormSet(prefix='clients'),
            'task_formset': TaskFormSet(prefix='tasks'),
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
        # client formset
        ClientFormSet = inlineformset_factory(ConstructionBid, Client, fields=("first_name","last_name",), extra=0, can_delete_extra=True)
        #task formset
        TaskFormSet = inlineformset_factory(ConstructionBid, Task, form=TaskForm, extra=1, can_delete_extra=True)

        #return redirect(self.success_url)
        construction_form = self.construction_form(request.POST, prefix='construction_bid')
        client_formset = ClientFormSet(request.POST, prefix='clients')
        task_formset = TaskFormSet(request.POST, prefix='tasks')

        if construction_form.is_valid() and client_formset.is_valid() and task_formset.is_valid():
            construction_bid = construction_form.save()

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
                'title': 'ModelFormClassCreateView Page',
                # 'page_id': 'model-form-class-id',
                # 'page_class': 'model-form-class-page',
                'h1_tag': 'This is the ModelFormClassCreateView Class Page Using ConstructionBidForm',
                'construction_form': construction_form,
                'client_formset': client_formset,
                'task_formset': task_formset,
                # 'phone_formset': PhoneFormSet,
                # 'client_form': self.client_form(),
            })