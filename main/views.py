from django.shortcuts import redirect
from django.contrib.auth.models import User

from main.models import Student, Professor, Administrator

# Create your views here.
def index(request):
    user = request.user

    # Redirecting to related page
    if isStudent(user) != None:
        return redirect("student:index")
    if isProfessor(user) != None:
        return redirect("professor:index")
    if isAdministrator(user) != None:
        return redirect("administrator:index")

    return redirect("login")


def isStudent(user):
    try:
        return Student.objects.get(id=user if isinstance(user, int) else user.id)
    except Student.DoesNotExist:
        return None
        

def isProfessor(user):
    try:
        return Professor.objects.get(id=user if isinstance(user, int) else user.id)
    except Professor.DoesNotExist:
        return None

def isAdministrator(user):
    try:
        return Administrator.objects.get(id=user if isinstance(user, int) else user.id)
    except Administrator.DoesNotExist:
        return None