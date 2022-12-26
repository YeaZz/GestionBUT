from django.urls import path
from student.views import *

app_name = 'student'

urlpatterns = [
    # http://domain/student/
    path('', index, name="index"),

    # http://domain/student/1/
    path('<resource_id>/', resource, name="resource"),
]
