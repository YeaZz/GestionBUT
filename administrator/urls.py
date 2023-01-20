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

    # http://domain/administrator/1/1/createCompetence/ (no template)
    path('<establishment_id>/<department_id>/createCompetence/', createCompetence, name="createCompetence"),

    # http://domain/administrator/1/1/createSemester/ (no template)
    path('<establishment_id>/<department_id>/createSemester/', createSemester, name="createSemester"),

    # http://domain/administrator/1/1/createGroup/ (no template)
    path('<establishment_id>/<department_id>/createGroup/', createGroup, name="createGroup"),
]