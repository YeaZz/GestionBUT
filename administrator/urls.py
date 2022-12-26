from django.urls import path
from administrator.views import *

app_name = 'administrator'

urlpatterns = [
    # http://domain/administrator/
    path('', index, name="index"),

    # http://domain/administrator/createEstablishment/ (no template)
    path('createEstablishment/', createEstablishment, name="createEstablishment"),
]