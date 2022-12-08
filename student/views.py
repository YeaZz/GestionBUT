from django.shortcuts import render
from main.models import UsefulLink
from main.views import isStudent

# Create your views here.
def index(request):
    user = request.user

    student = isStudent(user)

    if student != False:
        group = student.group.all().first()
        #semester = group.year.semester
        department = group.department
        establishment = department.establishment
        usefulLinks = UsefulLink.objects.all().filter(department_id=department.id)

        return render(request, "index.html", context={"user": user, "departement": department, "establishment": establishment, "usefulLinks": usefulLinks})
    return render(request, "index.html")

def page(request):
    return render(request, "page.html")