from django.urls import path
from professor.views import *

app_name = 'professor'

urlpatterns = [
    path('', index, name="index"),
    path('<department_id>/', department, name="department"),
]