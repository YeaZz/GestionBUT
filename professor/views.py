from django.shortcuts import render, redirect

from main.models import *
from main.views import isProfessor

# Create your views here.
def index(request):
    user = request.user
    professor = isProfessor(user)
    if professor == None:
        return redirect("login")

    esta_dpts_smtrs = {}
    establishments = professor.getEtablishments()
    for establishment in establishments:
        esta_dpts_smtrs[establishment] = {}
        departments = professor.departments.all()
        for department in departments:
            semesters = Semester.objects.filter(department=department)
            esta_dpts_smtrs[establishment][department] = semesters

    actual_semester = Semester.objects.filter(number=1).first()

    return render(
        request,
        "p_index.html",
        context={
            "user": user,
            "esta_dpts_smtrs": esta_dpts_smtrs,
            "actual_semester": actual_semester,
        }
    )

def department(request, department_id):
    user = request.user
    professor = isProfessor(user)
    if professor == None:
        return redirect("login")

    department = Department.objects.filter(id=department_id).first()
    if department == None:
        return redirect("professor:index")
    establishment = department.establishment

    semesters_ues_evals = {}
    semesters = Semester.objects.filter(department=department)
    for semester in semesters:
        semesters_ues_evals[semester] = {}
        ues = semester.ues.all()
        for ue in ues:
            evaluations = Evaluation.objects.filter(semester=semester, ues=ue)
            semesters_ues_evals[semester][ue] = evaluations

    usefulLinks = UsefulLink.objects.filter(department=department)

    return render(
        request,
        "department.html",
        context = {
            "establishment": establishment,
            "department": department,
            "semesters_ues_evals": semesters_ues_evals,
            "usefulLinks": usefulLinks,
        }
    )