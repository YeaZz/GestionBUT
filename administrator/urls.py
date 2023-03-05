from django.urls import path
from administrator.views import *

app_name = 'administrator'

urlpatterns = [
    # http://domain/administrator/
    path('', index, name="index"),

    # http://domain/administrator/createEstablishment/ (no template)
    path('createEstablishment/', createEstablishment, name="createEstablishment"),

    # http://domain/administrator/establishment/1/
    path('establishment/<establishment_id>/', establishment, name="establishment"),
    # http://domain/administrator/establishment/1/createDepartment/ (no template)
    path('establishment/<establishment_id>/createDepartment/', createDepartment, name="createDepartment"),
    #http://domain/administrator/establishment/1/department/1/
    path('establishment/<establishment_id>/department/<department_id>/', department, name="department"),


    # http://domain/administrator/establishment/1/department/1/createCompetence/ (no template)
    path('establishment/<establishment_id>/department/<department_id>/createCompetence/', createCompetence, name="createCompetence"),
    # http://domain/administrator/establishment/1/department/1/editCompetence/1/ (no template)
    path('establishment/<establishment_id>/department/<department_id>/editCompetence/<competence_id>/', editCompetence, name="editCompetence"),
    # http://domain/administrator/establishment/1/department/1/deleteCompetence/1/ (no template)
    path('establishment/<establishment_id>/department/<department_id>/deleteCompetence/<competence_id>/', deleteCompetence, name="deleteCompetence"),


    # http://domain/administrator/establishment/1/department/1/createSemester/ (no template)
    path('establishment/<establishment_id>/department/<department_id>/createSemester/', createSemester, name="createSemester"),
    # http://domain/administrator/establishment/1/department/1/editSemester/1/ (no template)
    path('establishment/<establishment_id>/department/<department_id>/editSemester/<semester_id>/', editSemester, name="editSemester"),
    # http://domain/administrator/establishment/1/department/1/deleteSemester/1/ (no template)
    path('establishment/<establishment_id>/department/<department_id>/deleteSemester/<semester_id>/', deleteSemester, name="deleteSemester"),


    # http://domain/administrator/establishment/1/department/1/createGroup (no template)
    path('establishment/<establishment_id>/department/<department_id>/createGroup', createGroup, name="createGroup"),
    # http://domain/administrator/establishment/1/department/1/editGroup/1/ (no template)
    path('establishment/<establishment_id>/department/<department_id>/editGroup/<group_id>/', editGroup, name="editGroup"),
    # http://domain/administrator/establishment/1/department/1/deleteGroup/1/ (no template)
    path('establishment/<establishment_id>/department/<department_id>/deleteGroup/<group_id>/', deleteGroup, name="deleteGroup"),
]