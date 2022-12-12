from django.urls import path
from administrator.views import index

app_name = 'administrator'

urlpatterns = [
    path('', index, name="index")
]