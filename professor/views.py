from django.shortcuts import render

from main.models import UsefulLink
from main.views import isProfessor

# Create your views here.
def index(request):
    user = request.user
    professor = isProfessor(user)

    if professor == None:
        return

    department = professor.department.first()
    establishment = department.establishment
    usefulLinks = UsefulLink.objects.all().filter(department_id=department.id)

    return render(request, "p_index.html", context={"user": user, "departement": department, "establishment": establishment, "usefulLinks": usefulLinks})

def groupetu(request):
    user = request.user
    return render(request, "groupetu.html", context={"user": user})