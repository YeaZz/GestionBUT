from django.urls import path
from student.views import *

app_name = 'student'

urlpatterns = [
    # http://domain/student/
    path('', index, name="index"),

    # http://domain/1/student/resource/1/
    path('<semester_id>/resource/<resource_id>/', resource, name="resource"),

    # http://domain/1/student/ue/1/
    path('<semester_id>/ue/<ue_id>/', ue, name="ue"),
]
