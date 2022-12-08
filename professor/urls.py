from django.urls import path
from professor.views import index

app_name = 'professor'

urlpatterns = [
    path('', index, name="index")
]