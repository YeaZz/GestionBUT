from django.shortcuts import redirect, HttpResponse

from main.models import Student, Professor

# Create your views here.
def index(request):
    user = request.user
    student = isStudent(user)
    if student != None:
        return redirect("student:index")

    professor = isProfessor(user)
    if professor != None:
        return redirect("professor:index")
    
    return HttpResponse(status=404)


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
