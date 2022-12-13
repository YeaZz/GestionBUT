from django.urls import path
from professor.views import index, groupetu

app_name = 'professor'

urlpatterns = [
    path('', index, name="index"),
    path('groupetu/',groupetu,name="groupetu")
]