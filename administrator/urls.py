from django.urls import path
from administrator.views import *

app_name = 'administrator'

urlpatterns = [
    path('', index, name="index"),
    path('establishment_gest/', establishmentgest, name="establishmentgest"),
    path('add_establishment/', addestablishment, name="addestablishment"),
    path('add_department/', adddepartment, name="adddepartment"),
    path('add_link/', addlink, name="addlink")
]