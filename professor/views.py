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
        for department in establishment.getDepartments():
            professor_view[establishment][department] = {}
            for semester in department.getSemesters():
                professor_view[establishment][department][semester] = semester.getProfessorResources(professor)

    return render(
        request,
        "p_index.html",
        context={
            "professor_view": professor_view
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
        for resource in semester.getProfessorResources(professor):
            professor_view[semester][resource] = resource.getEvaluations()

    return render(
        request,
        "department.html",
        context = {
            "professor_view": professor_view,
            "department": department,
            "usefulLinks": department.getUsefulLinks(),
        }
    )

def createNote(request, department_id, resource_id):
    user = request.user
    professor = isProfessor(user)
    if professor == None:
        return redirect("main:index")

    department = Department.objects.filter(id=department_id).first()
    resource = Resource.objects.filter(id=resource_id).first()
    if request.method != "POST" or department == None:
        return redirect("professor:index")
    elif resource == None:
        return redirect("professor:department", department_id=department.id)

    post = request.POST
    if "name" in post and "group" in post:
        group = post.get("group")
        if group != "none":
            evaluation = Evaluation(name=post.get("name"), professor=professor, resource=resource)
            evaluation.save()
            for str_student, note in post.items():
                if "note " + group in str_student:
                    user_id = int(str_student.split(" ")[2])
                    student = isStudent(user_id)
                    if student == None: continue
                    grade = Grade(evaluation=evaluation, student=student, note=float(note) if note != '' else None)
                    grade.save()

    return redirect("professor:department", department_id=department.id)