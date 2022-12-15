from django.shortcuts import render, redirect

from main.models import *
from main.views import isStudent

# Create your views here.
def index(request):
    user = request.user
    student = isStudent(user)

    if student == None:
        return redirect("accounts:login")

    group = student.groups.all().first()
    semesters = Semester.objects.all()
    department = group.department
    establishment = department.establishments.all().first()
    usefulLinks = UsefulLink.objects.all().filter(department_id=department.id)

    return render(
        request,
        "s_index.html",
        context = {
            "user": user,
            "departement": department,
            "establishment": establishment,
            "usefulLinks": usefulLinks,
            "semesters": semesters,
        }
    )

def evaluation(request, semester_id, ue_id):
    user = request.user
    student = isStudent(user)

    if student == None:
        return redirect("accounts:login")

    semester = Semester.objects.all().filter(id=semester_id).first()
    ue = UE.objects.all().filter(id=ue_id).first()

    if semester == None or ue == None:
        return redirect("student:index")

    evaluations = Evaluation.objects.all().filter(semester=semester_id, ue=ue_id)
    group = student.groups.all().first()
    department = group.department
    usefulLinks = UsefulLink.objects.all().filter(department_id=department.id)

    return render(
        request,
        "evaluation.html",
        context={
            "semester": semester,
            "ue": ue,
            "usefulLinks": usefulLinks,
            "evaluations": evaluations
        }
    )
