from django.urls import path
from student.views import index, evaluation

app_name = 'student'

urlpatterns = [
    path('', index, name="index"),
    path('<semester_id>/<ue_id>/', evaluation, name="evaluation"),
]