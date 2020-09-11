from datetime import timedelta

from django import forms
from django.forms import ValidationError
from django.conf import settings
from django.forms import ModelForm
from company.models import Company
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _

from django.forms import ModelForm

class CompanyProfile(ModelForm):
    class Meta:
        model = Company
        fields = ['company_name','company_regid', 'company_vatid', 'company_street1', 'company_street2', 'company_zipcode', 'company_city', 'company_country']