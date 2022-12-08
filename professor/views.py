from django.shortcuts import render
from django.template.loader import get_template

from main.models import UsefulLink
from main.views import isProfessor

# Create your views here.
def index(request):
    user = request.user
    professor = isProfessor(user)

    if professor == None:
        return

    departments = professor.departments

    return render(request, "p_index.html", context = {
            "user": user,
            "departements": departments,
        }
    )
