from django.shortcuts import redirect

from main.models import Student, Professor, Administrator

# Create your views here.
def index(request):
    user = request.user

    student = isStudent(user)
    if student != None:
        return redirect("student:index")

    professor = isProfessor(user)
    if professor != None:
        return redirect("professor:index")

    admin = isAdmin(user)
    if admin != None:
        return redirect("administrator:index")
    
    return redirect("login")


def isStudent(user):
    students = Student.objects.all();   #récupère tout les étudiants
    for student in students:
        if student.id.id == user.id:    #étudiant loopé est l'utilisateur donné en param
            return student              #retourne l'étudiant
    return None                         #sinon return None

def isProfessor(user):
    professors = Professor.objects.all();
    for professor in professors:
        if professor.id.id == user.id:
            return professor
    return None

def isAdmin(user):
    administrators = Administrator.objects.all();
    for administrator in administrators:
        if administrator.id.id == user.id:
            return administrator
    return None