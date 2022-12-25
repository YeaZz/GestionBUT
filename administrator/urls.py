from django.urls import path
from administrator.views import *

app_name = 'administrator'

urlpatterns = [
    path('', index, name="index"),
    path('createEstablishment/', createEstablishment, name="createEstablishment"),
]