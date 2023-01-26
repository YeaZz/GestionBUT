from django.shortcuts import render, redirect

from main.models import *
from main.views import isAdministrator

# Create your views here.
def index(request):
    admin = isAdministrator(request.user)
    if admin == None:
        return redirect("login")

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

def establishment(request, establishment_id):
    admin = isAdministrator(request.user)
    if admin == None:
        return redirect("login")

    establishment = Establishment.objects.filter(id=establishment_id).first()
    if establishment == None:
        return redirect("administrator:index")

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

def createEstablishment(request):
    admin = isAdministrator(request.user)
    if admin == None:
        return redirect("main:index")

    if request.method != "POST":
        return redirect("administrator:index")

    post = request.POST
    if "name" in post:
        name = post.get("name")
        if name != "":
            establishment = Establishment(name=name)
            establishment.save()
            if "it_department" in post:
                establishment.createITDepartment()
    return redirect("administrator:index")

def department(request, establishment_id, department_id):
    admin = isAdministrator(request.user)
    if admin == None:
        return redirect("login")

    establishment = Establishment.objects.filter(id=establishment_id).first()
    department = Department.objects.filter(id=department_id).first()
    if establishment == None:
        return redirect("administrator:index")
    elif department == None:
        return redirect("administrator:establishment", establishment.id)

    administrator_view = {}
    for department in establishment.getDepartments():
        administrator_view[department] = department.getSemesters()

    return render(
        request,
        "a_department.html",
        context= {
            "department": department,
            "competences": department.getCompetences(),
            "resources": department.getResources(),
            "semesters": department.getSemesters(),
            "groups": department.getGroups(),
            "administrator_view": administrator_view,
            "usefulLinks": department.getUsefulLinks()
        }
    )

def createDepartment(request, establishment_id):
    admin = isAdministrator(request.user)
    if admin == None:
        return redirect("main:index")

    establishment = Establishment.objects.filter(id=establishment_id).first()
    if establishment == None or request.method != "POST":
        return redirect("administrator:index")

    post = request.POST
    if "name" in post:
        name = post.get("name")
        if name != "":
            if "it_department" in post:
                establishment.createITDepartment(name)
            else:
                department = Department(name=name, establishment=establishment)
                department.save()

    return redirect("administrator:establishment", establishment_id=establishment.id)

def createCompetence(request, establishment_id, department_id):
    admin = isAdministrator(request.user)
    if admin == None:
        return redirect("main:index")

    establishment = Establishment.objects.filter(id=establishment_id).first()
    department = Department.objects.filter(id=department_id).first()
    if establishment == None:
        return redirect("administrator:index")
    elif department == None or request.method != "POST":
        return redirect("administrator:establishment", establishment_id)

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

def editCompetence(request, establishment_id, department_id, competence_id):
    admin = isAdministrator(request.user)
    if admin == None:
        return redirect("main:index")

    establishment = Establishment.objects.filter(id=establishment_id).first()
    department = Department.objects.filter(id=department_id).first()
    competence = Competence.objects.filter(id=competence_id).first()
    if establishment == None:
        return redirect("administrator:index")
    elif department == None or competence == None:
        return redirect("administrator:establishment", establishment_id)

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

def deleteCompetence(request, establishment_id, department_id, competence_id):
    admin = isAdministrator(request.user)
    if admin == None:
        return redirect("main:index")

    establishment = Establishment.objects.filter(id=establishment_id).first()
    department = Department.objects.filter(id=department_id).first()
    competence = Competence.objects.filter(id=competence_id).first()
    if establishment == None:
        return redirect("administrator:index")
    elif department == None or competence == None:
        return redirect("administrator:establishment", establishment_id)

    competence.delete()

    return redirect("administrator:department", establishment_id, department_id)






def createSemester(request, establishment_id, department_id):
    admin = isAdministrator(request.user)
    if admin == None:
        return redirect("main:index")

    establishment = Establishment.objects.filter(id=establishment_id).first()
    department = Department.objects.filter(id=department_id).first()
    if establishment == None:
        return redirect("administrator:index")
    elif department == None or request.method != "POST":
        return redirect("administrator:establishment", establishment_id)

    post = request.POST
    if "number" in post:
        str_number = post.get("number")
        semester = Semester(department=department, number=int(str_number))
        semester.save()

    return redirect("administrator:department", establishment_id, department_id)

def editSemester(request, establishment_id, department_id, semester_id):
    admin = isAdministrator(request.user)
    if admin == None:
        return redirect("main:index")

    establishment = Establishment.objects.filter(id=establishment_id).first()
    department = Department.objects.filter(id=department_id).first()
    semester = Semester.objects.filter(id=semester_id).first()
    if establishment == None:
        return redirect("administrator:index")
    elif department == None or semester == None:
        return redirect("administrator:establishment", establishment_id)

    post = request.POST
    if "number" in post:
        str_number = post.get("number")
        semester.number = int(str_number);
        semester.save()

    return redirect("administrator:department", establishment_id, department_id)

def deleteSemester(request, establishment_id, department_id, semester_id):
    admin = isAdministrator(request.user)
    if admin == None:
        return redirect("main:index")

    establishment = Establishment.objects.filter(id=establishment_id).first()
    department = Department.objects.filter(id=department_id).first()
    semester = Semester.objects.filter(id=semester_id).first()
    if establishment == None:
        return redirect("administrator:index")
    elif department == None or semester == None:
        return redirect("administrator:establishment", establishment_id)

    semester.delete()

    return redirect("administrator:department", establishment_id, department_id)







def createGroup(request, establishment_id, department_id):
    admin = isAdministrator(request.user)
    if admin == None:
        return redirect("main:index")

    establishment = Establishment.objects.filter(id=establishment_id).first()
    department = Department.objects.filter(id=department_id).first()
    if establishment == None:
        return redirect("administrator:index")
    elif department == None or request.method != "POST":
        return redirect("administrator:establishment", establishment_id)

    post = request.POST
    if "name" in post and "parent" in post:
        print(post)
        name = post.get("name")
        str_parent = post.get("parent")
        group = Group(department=department, name=name)
        if str_parent != "none":
            parent = Group.objects.filter(id=str_parent).first()
            if parent != None:
                group.parent = parent
        group.save()

    return redirect("administrator:department", establishment_id, department_id)

def editGroup(request, establishment_id, department_id, group_id):
    admin = isAdministrator(request.user)
    if admin == None:
        return redirect("main:index")

    establishment = Establishment.objects.filter(id=establishment_id).first()
    department = Department.objects.filter(id=department_id).first()
    group = Group.objects.filter(id=group_id).first()
    if establishment == None:
        return redirect("administrator:index")
    elif department == None or group == None:
        return redirect("administrator:establishment", establishment_id)

    post = request.POST
    if "name" in post and "parent" in post:
        name = post.get("name")
        str_parent = post.get("parent")
        if str_parent == "none":
            group.parent = None
        else:
            parent = Group.objects.filter(id=str_parent).first()
            if parent != None:
                group.parent = parent
        group.name = name
        group.save()

    return redirect("administrator:department", establishment_id, department_id)

def deleteGroup(request, establishment_id, department_id, group_id):
    admin = isAdministrator(request.user)
    if admin == None:
        return redirect("main:index")

    establishment = Establishment.objects.filter(id=establishment_id).first()
    department = Department.objects.filter(id=department_id).first()
    group = Group.objects.filter(id=group_id).first()
    if establishment == None:
        return redirect("administrator:index")
    elif department == None or group == None:
        return redirect("administrator:establishment", establishment_id)

    group.delete()

    return redirect("administrator:department", establishment_id, department_id)