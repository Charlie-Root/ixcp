from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, FormView
from django.forms import modelformset_factory
from company.models import Company
from django.urls import reverse
from django.urls import reverse_lazy
from django.forms.models import inlineformset_factory
from django.contrib.auth.models import User

from .forms import (
    CompanyProfile
)

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class ChangeCompanyProfileView(LoginRequiredMixin, FormView):
    
    form_class = CompanyProfile
    template_name = 'company/profile/change_profile.html'
    success_url = reverse_lazy('accounts:change_profile')
    
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def form_valid(self, form): 
        # This method is called when valid form data has been POSTed. 
        # It should return an HttpResponse. 
        form.instance.company_user = self.request.user
        self.object = form.save(commit=False)
        self.object.save()
        # perform a action here 
        print(form.cleaned_data) 
        return super().form_valid(form) 

    def send_mail(self, valid_data):
        # Send mail logic
        print(valid_data)
        pass
