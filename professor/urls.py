from django.urls import path
from professor.views import *

app_name = 'professor'

urlpatterns = [
    # http://domain/professor/
    path('', index, name="index"),

    # http://domain/professor/1/
    path('<department_id>/', department, name="department"),

    # http://domain/professor/1/1/
    path('<department_id>/<resource_id>/', resource, name="resource"),

    # http://domain/professor/createEvaluation/1/1/ (no template)
    path('createEvaluation/<department_id>/<resource_id>/', createEvaluation, name="createEvaluation"),

    # http://domain/professor/editEvaluation/1/1/1/ (no template)
    path('editEvaluation/<department_id>/<resource_id>/<evaluation_id>/', editEvaluation, name="editEvaluation"),

    # http://domain/professor/deleteEvaluation/1/1/1/ (no template)
    path('deleteEvaluation/<department_id>/<resource_id>/<evaluation_id>/', deleteEvaluation, name="deleteEvaluation"),
]
