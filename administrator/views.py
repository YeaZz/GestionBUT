from django.shortcuts import render, redirect

from main.models import *
from main.views import isAdministrator

# Create your views here.
def index(request):
    user = request.user
    admin = isAdministrator(user)
    if admin == None:
        return redirect("login")

    establishments = Establishment.objects.all()

    return render(request, "a_index.html", context = {
            "user": user,
            "establishments" : establishments,
        }
    )


def establishmentgest(request):
    user = request.user
    admin = isAdministrator(user)

    if admin == None:
        return

    establishments = Establishment.objects.all()

    return render(request, "establishmentgest.html", context = {
            "user": user,
            "establishments" : establishments,
        }
    )


def addestablishment(request):
    user = request.user
    admin = isAdministrator(user)
    if admin == None:
        return

    establishments = Establishment.objects.all()

    departments = Department.objects.all()

    return render(request, "addestablishment.html", context = {
            "user": user,
            "establishments" : establishments,
            "departments": departments
        }
    )

def adddepartment(request):
    user = request.user
    admin = isAdministrator(user)

    if admin == None:
        return

    establishments = Establishment.objects.all()
    departments = Department.objects.all()

    return render(request, "adddepartment.html", context = {
            "user": user,
            "establishments" : establishments,
            "departments": departments
        }
    )

def addlink(request):
    user = request.user
    admin = isAdministrator(user)

    if admin == None:
        return

    establishments = Establishment.objects.all()

    return render(request, "addlink.html", context = {
            "user": user,
            "establishments" : establishments,
        }
    )