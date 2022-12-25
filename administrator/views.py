from django.shortcuts import render, redirect

from main.models import *
from main.views import isAdministrator

# Create your views here.
def index(request):
    user = request.user
    admin = isAdministrator(user)
    if admin == None:
        return redirect("login")

    administrator_view = {}
    establishments = Establishment.objects.all()
    for establishment in establishments:
        administrator_view[establishment] = establishment.getDepartments()

    return render(request, "a_index.html", context = {
            "user": user,
            "administrator_view" : administrator_view,
        }
    )

def establishment(request, establishment_id):
    user = request.user
    admin = isAdministrator(user)
    if admin == None:
        return redirect("login")

    establishment = Establishment.objects.filter(id=establishment_id).first()
    if establishment == None:
        return redirect("administrator:index")

    administrator_view = {}
    for department in establishment.getDepartments():
        administrator_view[department] = department.getSemesters()

    return render(request, "department.html", context= {
            "user": user,
            "administrator_view": administrator_view
        }
    )

def createEstablishment(request):
    user = request.user
    admin = isAdministrator(user)
    if admin == None:
        return redirect("main:index")

    if request.method != "POST":
        return redirect("administrator:index")

    post = request.POST
    if "name" in post:
        establishment = Establishment(name=post.get("name"))
        establishment.save()
        if "it_department" in post:
            establishment.createITDepartment()

    return redirect("administrator:index")