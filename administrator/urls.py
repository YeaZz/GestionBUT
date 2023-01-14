from django.urls import path
from administrator.views import *

app_name = 'administrator'

urlpatterns = [
    # http://domain/administrator/
    path('', index, name="index"),

    # http://domain/administrator/createEstablishment/ (no template)
    path('createEstablishment/', createEstablishment, name="createEstablishment"),

    # http://domain/administrator/1/
    path('<establishment_id>/', establishment, name="establishment"),

    # http://domain/administrator/1/createDepartment/ (no template)
    path('<establishment_id>/createDepartment/', createDepartment, name="createDepartment"),

    #http://domain/administrator/1/1/
    path('<establishment_id>/<department_id>/', department, name="department"),
]