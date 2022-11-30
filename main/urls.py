from django.urls import path, include
from main.views import index

app_name = 'main'

urlpatterns = [
    path('', index, name="main")
]