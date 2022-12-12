from django.shortcuts import render, redirect

from main.models import UsefulLink, Semester
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
    establishment = department.establishment
    usefulLinks = UsefulLink.objects.all().filter(department_id=department.id)

<<<<<<< HEAD
    return render(request, "s_index.html", context = {
=======
    return render(
        request, 
        "s_index.html", 
        context = {
>>>>>>> cf257c996ac6271d829708a7d9ac7cb76bb62d75
            "user": user,
            "departement": department,
            "establishment": establishment,
            "usefulLinks": usefulLinks,
            "semesters": semesters,
        }
    )

def page(request):
    return render(request, "page.html")