from django.shortcuts import render, redirect

from main.models import *
from main.views import isProfessor

# Create your views here.
def index(request):
    user = request.user
    professor = isProfessor(user)
    #student=isStudent(user)

    if professor == None:
        return redirect("login")#modifié

    establishments = professor.establishments.all()

    eta_dpt_grps = {}
    for establishment in establishments:
        eta_dpt_grps[establishment] = {}
        for department in establishment.departments.all():
            eta_dpt_grps[establishment][department] = {}
            promos = Group.objects.all().filter(parent=None, department=department.id)
            for promo in promos:
                eta_dpt_grps[establishment][department][promo] = Group.objects.all().filter(parent=promo, department=department.id)
                
    print(eta_dpt_grps)
    return render(
        request,
        "p_index.html",
        context={
            "user": user,
            "establishments": establishments,
            "promos":promos,
            "eta_dpt_grps":eta_dpt_grps
        }
    )

def testGroup(Group): #fonction qui supprime les groupe ayant un parent (ne garde que la promotion)
    TempGroupe=Group
    for p in TempGroupe:
        if(p.parent!=None):
            p.delete()
    return TempGroupe;#retourne un QuerySet sans sous-groupe

def groupEtu(request):
    user = request.user
    return render(request, "groupetu.html", context={"user": user})

def ajoutNote(request):
    user=request.user
    return render(request,"ajoutnote.html",context={"user":user})