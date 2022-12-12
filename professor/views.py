from django.shortcuts import render, redirect

from main.models import UsefulLink
from main.views import isProfessor

# Create your views here.
def index(request):
    user = request.user
    professor = isProfessor(user)

    if professor == None:
        return redirect("accounts:login")

<<<<<<< HEAD
    department = professor.department.first()
    establishment = department.establishment
    usefulLinks = UsefulLink.objects.all().filter(department_id=department.id)

    return render(request, "p_index.html", context={"user": user, "departement": department, "establishment": establishment, "usefulLinks": usefulLinks})

def groupetu(request):
    user = request.user
    return render(request, "groupetu.html", context={"user": user})
=======
    departments = professor.departments

    return render(request, "p_index.html", context = {
            "user": user,
            "departements": departments,
        }
    )
>>>>>>> cf257c996ac6271d829708a7d9ac7cb76bb62d75
