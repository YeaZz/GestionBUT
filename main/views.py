from django.shortcuts import redirect

from main.models import Student, Professor, Administrator

# Create your views here.
def index(request):
    user = request.user

    # Redirecting to related pages
    if isStudent(user) != None:
        return redirect("student:index")
    if isProfessor(user) != None:
        return redirect("professor:index")
    if isAdministrator(user) != None:
        return redirect("administrator:index")

    return redirect("login")


def isStudent(user):
    try:
        return Student.objects.get(id=user)
    except Student.DoesNotExist:
        return None

def isProfessor(user):
    try:
        return Professor.objects.get(id=user)
    except Professor.DoesNotExist:
        return None

def isAdministrator(user):
    try:
        return Administrator.objects.get(id=user)
    except Administrator.DoesNotExist:
        return None