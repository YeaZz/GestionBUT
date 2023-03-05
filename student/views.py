from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from main.models import *
from main.views import isStudent

@login_required
def index(request):
    user = request.user
    student = isStudent(user)
    if student == None:
        return redirect("login")

    department = student.department

    student_view = {}
    for semester in department.getSemesters():
        student_view[semester] = {}, {}

        # Vue ressource
        for resource in semester.getResources():
            student_view[semester][0][resource] = {}, resource.getNote(student), resource.getRanking(student)
            for evaluation in resource.getEvaluations():
                student_view[semester][0][resource][0][evaluation] = evaluation.getNote(student)

        # Vue UE
        for ue in semester.getUEs():
            student_view[semester][1][ue] = {}, ue.getNote(student), ue.getRanking(student)
            for resource in ue.getResources():
                student_view[semester][1][ue][0][resource] = {}
                for evaluation in resource.getEvaluations():
                    student_view[semester][1][ue][0][resource][evaluation] = evaluation.getNote(student)

    return render(
        request,
        "s_index.html",
        context = {
            "establishment": department.establishment,
            "student_view": student_view,
            "lastGrades": student.getLastGrades(5),
            "validate": department.validateYear(student),
            "usefulLinks": department.getUsefulLinks(),
        }
    )

@login_required
def resource(request, semester_id, resource_id):
    user = request.user
    student = isStudent(user)
    if student == None:
        return redirect("login")

    semester = Semester.objects.filter(id=semester_id).first()
    resource = Resource.objects.filter(id=resource_id).first()
    if semester == None or resource == None:
        return redirect("student:index")

    student_view = {}
    for evaluation in resource.getEvaluations():
        student_view[evaluation] = (
            evaluation.getNote(student),
            evaluation.getRanking(student),
            evaluation.getAverage(),
            evaluation.getMax(),
            evaluation.getMin()
        )

    return render(
        request,
        "s_resource.html",
        context={
            "semester": semester,
            "resource": resource,
            "student_view": student_view,
            "lastGrades": student.getLastGrades(5),
            "validate": semester.department.validateYear(student),
            "usefulLinks": student.department.getUsefulLinks(),
        }
    )

@login_required
def ue(request, semester_id, ue_id):
    user = request.user
    student = isStudent(user)
    if student == None:
        return redirect("login")

    semester = Semester.objects.filter(id=semester_id).first()
    ue = UE.objects.filter(id=ue_id).first()
    if semester == None or ue == None:
        return redirect("student:index")

    student_view = {}
    for resource in ue.getResources():
        student_view[resource] = {}
        for evaluation in resource.getEvaluations():
            student_view[resource][evaluation] = (
                evaluation.getNote(student),
                evaluation.getRanking(student),
                evaluation.getAverage(),
                evaluation.getMax(),
                evaluation.getMin()
            )

    return render(
        request,
        "s_ue.html",
        context={
            "semester": semester,
            "ue": ue,
            "student_view": student_view,
            "lastGrades": student.getLastGrades(5),
            "validate": semester.department.validateYear(student),
            "usefulLinks": student.department.getUsefulLinks(),
        }
    )