from django.shortcuts import render

from main.models import UsefulLink, Semester
from main.views import isStudent

# Create your views here.
def index(request):
    user = request.user
    student = isStudent(user)

    if student == None:
        return

    group = student.group.all().first()
    semesters = Semester.objects.all()
    department = group.department
    establishment = department.establishment
    usefulLinks = UsefulLink.objects.all().filter(department_id=department.id)

    return render(request, "index.html", context = {
            "user": user,
            "departement": department,
            "establishment": establishment,
            "usefulLinks": usefulLinks,
            "semesters": semesters
        }
    )
