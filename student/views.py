from django.shortcuts import render, redirect

from main.models import *
from main.views import isStudent

# Create your views here.
def index(request):
    user = request.user
    student = isStudent(user)
    if student == None:
        return redirect("login")

    department = student.department
    establishment = department.establishment
    usefulLinks = department.getUsefulLinks()

    student_view = {}
    for semester in department.getSemesters():
        student_view[semester] = {}, {}

        for resource in semester.getResources():
            student_view[semester][0][resource] = {}, resource.getNote(student), resource.getRanking(student)
            for evaluation in resource.getEvaluations():
                student_view[semester][0][resource][0][evaluation] = evaluation.getNote(student)

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
            "user": user,
            "establishment": establishment,
            "student_view": student_view,
            "lastGrades": student.getLastGrades(5),
            "usefulLinks": usefulLinks,
        }
    )

def resource(request, resource_id):
    user = request.user
    student = isStudent(user)
    if student == None:
        return redirect("login")

    resource = Resource.objects.filter(id=resource_id).first()
    if resource == None:
        return redirect("student:index")

    evaluations = Evaluation.objects.filter(resource=resource)
    evaluations_stats = {}
    for evaluation in evaluations:
        evaluations_stats[evaluation] = (
            evaluation.getNote(student),
            evaluation.getRanking(student),
            evaluation.getAverage(),
            evaluation.getMax(),
            evaluation.getMin()
        )

    department = student.department
    usefulLinks = department.getUsefulLinks()

    return render(
        request,
        "resource.html",
        context={
            "resource": resource,
            "evaluations": evaluations_stats,
            "lastGrades": student.getLastGrades(5),
            "usefulLinks": usefulLinks,
        }
    )
