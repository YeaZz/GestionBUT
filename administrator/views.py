from django.shortcuts import render, redirect
from django.template.loader import get_template

from main.models import *
from main.views import isAdmin

# Create your views here.
def index(request):
    user = request.user
    admin = isAdmin(user)

    if admin == None:
        return redirect("accounts:login")

    establishments = Establishment.objects.all()

    return render(request, "a_index.html", context = {
            "user": user,
            "establishments" : establishments,
        }
    )


def establishmentgest(request):
    user = request.user
    admin = isAdmin(user)

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
    admin = isAdmin(user)

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
    admin = isAdmin(user)

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
    admin = isAdmin(user)

    if admin == None:
        return

    establishments = Establishment.objects.all()

    return render(request, "addlink.html", context = {
            "user": user,
            "establishments" : establishments,
        }
    )