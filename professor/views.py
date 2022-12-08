from django.shortcuts import render

from main.models import UsefulLink
from main.views import isProfessor

# Create your views here.
def index(request):
    user = request.user
    professor = isProfessor(user)

    if professor == None:
        return

    department = professor.deparment.first()
    establishment = department.establishment
    usefulLinks = UsefulLink.objects.all().filter(department_id=department.id)

    return render(request, "index.html", context={"user": user, "departement": department, "establishment": establishment, "usefulLinks": usefulLinks})
