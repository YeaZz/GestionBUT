from django.urls import path
from professor.views import *

app_name = 'professor'

urlpatterns = [
    # http://domain/professor/
    path('', index, name="index"),

    # http://domain/professor/1/
    path('<department_id>/', department, name="department"),

    # http://domain/professor/1/1/ (no template)
    path('createNote/<department_id>/<resource_id>/', createNote, name="createNote")
]
