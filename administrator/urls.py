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

    # http://domain/administrator/createCompetence/1/1/ (no template)
    path('createCompetence/<establishment_id>/<department_id>/', createCompetence, name="createCompetence"),

    # http://domain/administrator/editCompetence/1/1/ (no template)
    path('editCompetence/<establishment_id>/<department_id>/<competence_id>/', editCompetence, name="editCompetence"),

    # http://domain/administrator/deleteCompetence/1/1/ (no template)
    path('deleteCompetence/<establishment_id>/<department_id>/<competence_id>/', deleteCompetence, name="deleteCompetence"),




    # http://domain/administrator/createSemester/1/1/ (no template)
    path('createSemester/<establishment_id>/<department_id>/', createSemester, name="createSemester"),

    # http://domain/administrator/editSemester/1/1/ (no template)
    path('editSemester/<establishment_id>/<department_id>/<semester_id>/', editSemester, name="editSemester"),

    # http://domain/administrator/deleteSemester/1/1/ (no template)
    path('deleteSemester/<establishment_id>/<department_id>/<semester_id>/', deleteSemester, name="deleteSemester"),



    # http://domain/administrator/createGroup/1/1/ (no template)
    path('createGroup/<establishment_id>/<department_id>/', createGroup, name="createGroup"),

    # http://domain/administrator/editGroup/1/1/ (no template)
    path('editGroup/<establishment_id>/<department_id>/<group_id>/', editGroup, name="editGroup"),

    # http://domain/administrator/deleteGroup/1/1/ (no template)
    path('deleteGroup/<establishment_id>/<department_id>/<group_id>/', deleteGroup, name="deleteGroup"),
]