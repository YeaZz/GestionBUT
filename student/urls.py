from django.urls import path
from student.views import *

app_name = 'student'

urlpatterns = [
    path('', index, name="index"),
    path('<resource_id>/', resource, name="resource"),
]