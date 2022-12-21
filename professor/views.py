from django.shortcuts import render, redirect

from main.models import *
from main.views import isProfessor, isStudent

# Create your views here.
def index(request):
    user = request.user
    professor = isProfessor(user)
    if professor == None:
        return redirect("login")

    professor_view = {}
    for establishment in professor.getEtablishments():
        professor_view[establishment] = {}
        for department in professor.getDepartments():
            professor_view[establishment][department] = {}
            for semester in department.getSemesters():
                professor_view[establishment][department][semester] = semester.getResources()

    return render(
        request,
        "p_index.html",
        context={
            "user": user,
            "professor_view": professor_view,
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

    professor_view = {}
    for semester in department.getSemesters():
        professor_view[semester] = {}
        for resource in semester.getResources():
            professor_view[semester][resource] = resource.getEvaluations()

    usefulLinks = UsefulLink.objects.filter(department=department)

    return render(
        request,
        "department.html",
        context = {
            "department": department,
            "professor_view": professor_view,
            "usefulLinks": usefulLinks,
        }
    )

def createNote(request, department_id, resource_id):
    user = request.user
    professor = isProfessor(user)
    if professor == None:
        return redirect("login")

    department = Department.objects.filter(id=department_id).first()
    resource = Resource.objects.filter(id=resource_id).first()
    if request.method != "POST" or department == None:
        return redirect("professor:index")
    elif resource == None:
        return redirect("professor:department", department_id=department.id)

    post = request.POST
    if post.__contains__("name") and post.__contains__("group"):
        evaluation = Evaluation(name=post.get("name"), professor=professor, resource=resource)
        evaluation.save()
        for student, note in post.items():
            if "note " + post.get("group") in student:
                user_id = int(student.split(" ")[2])
                student = isStudent(user_id)
                if student == None: continue
                grade = Grade(evaluation=evaluation, student=student, note=float(note))
                grade.save()

    return redirect("professor:department", department_id=department.id)