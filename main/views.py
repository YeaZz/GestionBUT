from django.shortcuts import render

from main.models import Establishment, UsefulLink, Student

# Create your views here.
def index(request):
    user = request.user

    student = isStudent(user)

    if student != False:
        department = student.group.all().first().department

        establishment = department.establishment

        usefulLinks = UsefulLink.objects.all().filter(department_id=department.id)

        return render(request, "student_view.html", context={"user": user, "departement": department, "establishment": establishment, "usefulLinks": usefulLinks})

    return render(request, "main.html")

def isStudent(user):
    students = Student.objects.all();   #récupère tout les étudiants
    for student in students:
        if student.id.id == user.id:    #étudiant loopé est l'utilisateur donné en param
            return student;             #retourne l'étudiant
    return False;                       #sinon return False
