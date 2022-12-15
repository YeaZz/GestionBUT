from django.shortcuts import render, redirect

from main.models import *
from main.views import isProfessor

# Create your views here.
def index(request):
    user = request.user
    professor = isProfessor(user)

    if professor == None:
        return redirect("login")

    establishments = professor.establishments.all()

    eta_dpt_grps = {}
    for establishment in establishments:
        eta_dpt_grps[establishment] = {}
        for department in establishment.departments.all():
            eta_dpt_grps[establishment][department] = {}
            promos = Group.objects.all().filter(parent=None, department=department.id)
            for promo in promos:
                eta_dpt_grps[establishment][department][promo] = Group.objects.all().filter(parent=promo, department=department.id)

    return render(
        request,
        "p_index.html",
        context={
            "user": user,
            "establishments": establishments,
            "promos": promos,
            "eta_dpt_grps": eta_dpt_grps,
        }
    )

def groupEtu(request):
    user = request.user
    return render(
        request,
        "groupetu.html",
        context = {
            "user": user
        }
    )

def ajoutNote(request):
    user=request.user
    return render(
        request,
        "ajoutnote.html",
        context = {
            "user": user
        }
    )