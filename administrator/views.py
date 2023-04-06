from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from main.models import *
from main.views import isAdministrator

@login_required
def index(request):

    # Auth security
    if isAdministrator(request.user) == None:
        return redirect("main:index")

    # Method body
    administrator_view = {}
    establishments = Establishment.objects.all()
    for establishment in establishments:
        administrator_view[establishment] = establishment.getDepartments()

    return render(
        request,
        "a_index.html",
        context = {
            "administrator_view" : administrator_view,
        }
    )

@login_required
def establishment(request, establishment_id):

    # Auth security
    if isAdministrator(request.user) == None:
        return redirect("main:index")

    # Query parameters
    establishment = Establishment.objects.get(id=establishment_id)
    if establishment == None:
        return redirect("administrator:index")

    # Method body
    administrator_view = {}
    for department in establishment.getDepartments():
        administrator_view[department] = department.getSemesters()

    return render(
        request,
        "a_establishment.html",
        context= {
            "establishment": establishment,
            "administrator_view": administrator_view
        }
    )

@login_required
def createEstablishment(request):
    # Auth security
    if isAdministrator(request.user) == None or request.method != "POST":
        return redirect("main:index")

    # Method body
    post = request.POST
    if "name" in post:
        name = post.get("name")
        if name != "":
            establishment = Establishment(name=name)
            establishment.save()
            if "it_department" in post:
                establishment.createITDepartment()

    return redirect("administrator:index")

@login_required
def department(request, establishment_id, department_id):

    # Auth security
    if isAdministrator(request.user) == None:
        return redirect("login")

    # Query parameters
    establishment = Establishment.objects.get(id=establishment_id)
    department = Department.objects.get(id=department_id)
    if establishment == None:
        return redirect("administrator:index")
    elif department == None:
        return redirect("administrator:establishment", establishment.id)

    # Method body
    administrator_view = {}
    for department in establishment.getDepartments():
        administrator_view[department] = department.getSemesters()

    return render(
        request,
        "a_department.html",
        context= {
            "establishment": establishment,
            "department": department,
            "administrator_view": administrator_view,
        }
    )


@login_required
def createDepartment(request, establishment_id):

    # Auth security
    if isAdministrator(request.user) == None:
        return redirect("main:index")

    # Query parameters
    establishment = Establishment.objects.get(id=establishment_id)
    if establishment == None or request.method != "POST":
        return redirect("administrator:index")

    # Method body
    post = request.POST
    if "name" in post and "min_competence_grade" in post and "min_competence_required" in post:
        name = post.get("name")
        str_min_competence_grade = post.get("min_competence_grade")
        str_min_competence_required = post.get("min_competence_required")
        if "it_department" in post:
            establishment.createITDepartment()
        elif name != "":
            department = Department(name=name, establishment=establishment, min_competence_grade=int(str_min_competence_grade), min_competence_required=int(str_min_competence_required))
            department.save()

    return redirect("administrator:establishment", establishment_id=establishment.id)

@login_required
def createCompetence(request, establishment_id, department_id):

    # Auth security
    if isAdministrator(request.user) == None:
        return redirect("main:index")

    # Query parameters
    establishment = Establishment.objects.get(id=establishment_id)
    department = Department.objects.get(id=department_id)
    if establishment == None:
        return redirect("administrator:index")
    elif department == None or request.method != "POST":
        return redirect("administrator:establishment", establishment_id)

    # Method body
    post = request.POST
    if "name" in post and "number" in post:
        name = post.get("name")
        str_number = post.get("number")
        competence = Competence(department=department, number=int(str_number), name=name)
        if "description" in post:
            description = post.get("description")
            if description != "":
                competence.description = description
        competence.save()

    return redirect("administrator:department", establishment_id, department_id)

@login_required
def editCompetence(request, establishment_id, department_id, competence_id):

    # Auth security
    if isAdministrator(request.user) == None:
        return redirect("main:index")

    # Query parameters
    establishment = Establishment.objects.get(id=establishment_id)
    department = Department.objects.get(id=department_id)
    competence = Competence.objects.get(id=competence_id)
    if establishment == None:
        return redirect("administrator:index")
    elif department == None or competence == None:
        return redirect("administrator:establishment", establishment_id)

    # Method body
    post = request.POST
    if  "number" in post and "name" in post and "description" in post:
        str_number = post.get("number")
        name = post.get("name")
        description = post.get("description")
        competence.number = int(str_number)
        competence.name = name
        competence.description = description
        competence.save()

    return redirect("administrator:department", establishment_id, department_id)

@login_required
def deleteCompetence(request, establishment_id, department_id, competence_id):

    # Auth security
    if isAdministrator(request.user) == None:
        return redirect("main:index")

    # Query parameters
    establishment = Establishment.objects.get(id=establishment_id)
    department = Department.objects.get(id=department_id)
    competence = Competence.objects.get(id=competence_id)
    if establishment == None:
        return redirect("administrator:index")
    elif department == None or competence == None:
        return redirect("administrator:establishment", establishment_id)

    # Method body
    competence.delete()

    return redirect("administrator:department", establishment_id, department_id)






@login_required
def createSemester(request, establishment_id, department_id):

    # Auth security
    admin = isAdministrator(request.user)
    if admin == None:
        return redirect("main:index")

    # Query parameters
    establishment = Establishment.objects.get(id=establishment_id)
    department = Department.objects.get(id=department_id)
    if establishment == None:
        return redirect("administrator:index")
    elif department == None or request.method != "POST":
        return redirect("administrator:establishment", establishment_id)

    # Method body
    post = request.POST
    if "number" in post:
        str_number = post.get("number")
        semester = Semester(department=department, number=int(str_number))
        semester.save()

    return redirect("administrator:department", establishment_id, department_id)

@login_required
def editSemester(request, establishment_id, department_id, semester_id):

    # Auth security
    admin = isAdministrator(request.user)
    if admin == None:
        return redirect("main:index")

    # Query parameters
    establishment = Establishment.objects.get(id=establishment_id)
    department = Department.objects.get(id=department_id)
    semester = Semester.objects.get(id=semester_id)
    if establishment == None:
        return redirect("administrator:index")
    elif department == None or semester == None:
        return redirect("administrator:establishment", establishment_id)

    # Method body
    post = request.POST
    if "number" in post:
        str_number = post.get("number")
        semester.number = int(str_number);
        semester.save()

    return redirect("administrator:department", establishment_id, department_id)

@login_required
def deleteSemester(request, establishment_id, department_id, semester_id):

    # Auth security
    admin = isAdministrator(request.user)
    if admin == None:
        return redirect("main:index")

    # Query parameters
    establishment = Establishment.objects.get(id=establishment_id)
    department = Department.objects.get(id=department_id)
    semester = Semester.objects.get(id=semester_id)
    if establishment == None:
        return redirect("administrator:index")
    elif department == None or semester == None:
        return redirect("administrator:establishment", establishment_id)

    # Method body
    semester.delete()

    return redirect("administrator:department", establishment_id, department_id)







@login_required
def createGroup(request, establishment_id, department_id):

    # Auth security
    admin = isAdministrator(request.user)
    if admin == None:
        return redirect("main:index")

    # Query parameters
    establishment = Establishment.objects.get(id=establishment_id)
    department = Department.objects.get(id=department_id)
    if establishment == None:
        return redirect("administrator:index")
    elif department == None or request.method != "POST":
        return redirect("administrator:establishment", establishment_id)

    # Method body
    post = request.POST
    if "name" in post and "parent" in post:
        print(post)
        name = post.get("name")
        str_parent = post.get("parent")
        group = Group(department=department, name=name)
        if str_parent != "none":
            parent = Group.objects.get(id=str_parent)
            if parent != None:
                group.parent = parent
        group.save()

    return redirect("administrator:department", establishment_id, department_id)

@login_required
def editGroup(request, establishment_id, department_id, group_id):

    # Auth security
    admin = isAdministrator(request.user)
    if admin == None:
        return redirect("main:index")

    # Query parameters
    establishment = Establishment.objects.get(id=establishment_id)
    department = Department.objects.get(id=department_id)
    group = Group.objects.get(id=group_id)
    if establishment == None:
        return redirect("administrator:index")
    elif department == None or group == None:
        return redirect("administrator:establishment", establishment_id)

    # Method body
    post = request.POST
    if "name" in post and "parent" in post:
        name = post.get("name")
        str_parent = post.get("parent")
        if str_parent == "none":
            group.parent = None
        else:
            parent = Group.objects.get(id=str_parent)
            if parent != None:
                group.parent = parent
        group.name = name
        group.save()

    return redirect("administrator:department", establishment_id, department_id)

@login_required
def deleteGroup(request, establishment_id, department_id, group_id):

    # Auth security
    admin = isAdministrator(request.user)
    if admin == None:
        return redirect("main:index")

    # Query parameters
    establishment = Establishment.objects.get(id=establishment_id)
    department = Department.objects.get(id=department_id)
    group = Group.objects.get(id=group_id)
    if establishment == None:
        return redirect("administrator:index")
    elif department == None or group == None:
        return redirect("administrator:establishment", establishment_id)

    # Method body
    group.delete()

    return redirect("administrator:department", establishment_id, department_id)