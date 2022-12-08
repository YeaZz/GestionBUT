from django.urls import path
from student.views import index, page

app_name = 'student'

urlpatterns = [
    path('', index, name="index"),
    path('page/', page, name="page")
]