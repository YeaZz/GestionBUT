from django.shortcuts import render, redirect
from django.template.defaulttags import register
from django.contrib.auth.decorators import login_required

from main.models import *
from main.views import isProfessor, isStudent

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter
def get_float(float):
    if (float == None):
        return ""
    return str(float).replace(",", ".")

@login_required
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

@login_required
def department(request, department_id):
    user = request.user
    professor = isProfessor(user)
    if professor == None:
        return redirect("login")

    department = Department.objects.filter(id=department_id).first()
    if department == None:
        return redirect("professor:index")

    professor_view = {}
    professor_resources = {}
    for semester in department.getSemesters():
        professor_view[semester] = {}
        professor_resources[semester] = []
        for resource in semester.getResources():
            professor_view[semester][resource] = {}
            for evaluation in resource.getEvaluations():
                professor_view[semester][resource][evaluation] = {}
                for grade in evaluation.getGrades():
                    professor_view[semester][resource][evaluation][grade.student] = grade.note
        for resource in semester.getProfessorResources(professor):
            professor_resources[semester].append(resource)

    return render(
        request,
        "p_department.html",
        context = {
            "students": department.getStudents(),
            "professor_view": professor_view,
            "professor_resources": professor_resources,
            "department": department,
            "usefulLinks": department.getUsefulLinks(),
        }
    )

@login_required
def resource(request, department_id, resource_id):
    user = request.user
    professor = isProfessor(user)
    if professor == None:
        return redirect("login")

    department = Department.objects.filter(id=department_id).first()
    resource = Resource.objects.filter(id=resource_id).first()
    if department == None:
        return redirect("professor:index")
    elif resource == None:
        return redirect("professor:department", department_id=department_id)

    professor_view = {}
    grades = {}
    for evaluation in resource.getEvaluations():
        grades[evaluation] = {}
        for grade in evaluation.getGrades():
            grades[evaluation][grade.student] = grade.note
        professor_view[evaluation] = (
            evaluation.getAverage(),
            evaluation.getMax(),
            evaluation.getMin(),
        )

    return render(
        request,
        "p_resource.html",
        context= {
            "professor_view": professor_view,
            "grades": grades,
            "department": department,
            "resource": resource,
            "usefulLinks": department.getUsefulLinks(),
        }
    )

@login_required
def createEvaluation(request, department_id, resource_id):
    user = request.user
    professor = isProfessor(user)
    if professor == None:
        return redirect("main:index")

    department = Department.objects.filter(id=department_id).first()
    resource = Resource.objects.filter(id=resource_id).first()
    if request.method != "POST" or department == None:
        return redirect("professor:index")
    elif resource == None or resource not in professor.getResources(department):
        return redirect("professor:department", department_id=department.id)

    post = request.POST
    if "name" in post and "max_note" in post and "coef" in post and "group" in post:
        name = post.get("name")
        max_note = int(post.get("max_note"))
        coef = float(post.get("coef"))
        str_group = post.get("group")
        group = Group.objects.filter(id=int(str_group)).first()
        if name != "" and str_group != "none" and group != None:
            evaluation = Evaluation(name=name, max_note=max_note, coef=coef, professor=professor, resource=resource, group=group)
            evaluation.save()
            for str_student, note in post.items():
                if "note " + str_group in str_student:
                    user_id = int(str_student.split(" ")[2])
                    student = isStudent(user_id)
                    if student == None: continue
                    grade = Grade(evaluation=evaluation, student=student, note=float(note) if note != '' else None)
                    grade.save()

    return redirect("professor:department", department_id=department_id)

@login_required
def editEvaluation(request, department_id, resource_id, evaluation_id):
    user = request.user
    professor = isProfessor(user)
    if professor == None:
        return redirect("main:index")

    department = Department.objects.filter(id=department_id).first()
    resource = Resource.objects.filter(id=resource_id).first()
    evaluation = Evaluation.objects.filter(id=evaluation_id).first()
    if request.method != "POST" or department == None:
        return redirect("professor:index")
    elif resource == None or resource not in professor.getResources(department) or evaluation == None:
        return redirect("professor:department", department_id=department.id)

    post = request.POST
    if "group" in post and "coef" in post:
        str_group = post.get("group")
        group = Group.objects.filter(id=str_group).first()
        coef = float(post.get("coef"))
        if group != None:
            evaluation.group = group
            evaluation.coef = coef
            evaluation.save()
            for str_student, note in post.items():
                if "note " + str_group in str_student:
                    user_id = int(str_student.split(" ")[2])
                    student = isStudent(user_id)
                    if student == None: continue
                    note = float(note) if note != '' else None
                    grade = evaluation.getGrade(student)
                    if grade != None:
                        grade.note = note
                        grade.save()
                    else:
                        grade = Grade(evaluation=evaluation, student=student, note=note)
                        grade.save()

    return redirect("professor:department", department_id=department_id)

@login_required
def deleteEvaluation(request, department_id, resource_id, evaluation_id):
    user = request.user
    professor = isProfessor(user)
    if professor == None:
        return redirect("main:index")

    department = Department.objects.filter(id=department_id).first()
    resource = Resource.objects.filter(id=resource_id).first()
    evaluation = Evaluation.objects.filter(id=evaluation_id).first()
    if request.method != "POST" or department == None:
        return redirect("professor:index")
    elif resource == None or resource not in professor.getResources(department) or evaluation == None:
        return redirect("professor:department", department_id=department.id)

    evaluation.delete()

    return redirect("professor:department", department_id=department_id)