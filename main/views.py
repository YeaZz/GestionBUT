from django.shortcuts import render, redirect
from main.models import Student

# Create your views here.
def index(request):
    user = request.user
    student = isStudent(user)
    if student != False:
        return redirect('student:index')
    return render(request, "main.html")

def isStudent(user):
    students = Student.objects.all();   #récupère tout les étudiants
    for student in students:
        if student.id.id == user.id:    #étudiant loopé est l'utilisateur donné en param
            return student;             #retourne l'étudiant
    return False;                       #sinon return False
