from django.urls import path
from professor.views import *

app_name = 'professor'

urlpatterns = [
    path('', index, name="index"),
    path('groupetu/', groupEtu, name="groupetu"),
    path('ajoutnote/', ajoutNote, name="ajoutnote"),
]