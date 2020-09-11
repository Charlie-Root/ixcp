from django.urls import path

from . import views

from .views import (
   ChangeCompanyProfileView
)

urlpatterns = [
    path('', views.index, name='log_in'),
    path('change/profile/', ChangeCompanyProfileView.as_view(), name='change_profile'),
   
]
