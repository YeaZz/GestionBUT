from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User

from main.models import Student, Professor, Administrator

def index(request: HttpResponse):
    user = request.user

    # Redirecting to related page
    if isStudent(user) != None:
        return redirect("student:index")
    if isProfessor(user) != None:
        return redirect("professor:index")
    if isAdministrator(user) != None:
        return redirect("administrator:index")

    return redirect("login")


def isStudent(user: User) -> None | Student:
    try:
        return Student.objects.get(id=user if isinstance(user, int) else user.id)
    except Student.DoesNotExist:
        return None

def isProfessor(user: User) -> None | Professor:
    try:
        return Professor.objects.get(id=user if isinstance(user, int) else user.id)
    except Professor.DoesNotExist:
        return None

def isAdministrator(user: User) -> None | Administrator:
    try:
        return Administrator.objects.get(id=user if isinstance(user, int) else user.id)
    except Administrator.DoesNotExist:
        return None