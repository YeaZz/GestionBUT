from django.shortcuts import render
from django.template.loader import get_template

from main.models import UsefulLink
from main.views import isAdmin

# Create your views here.
def index(request):
    user = request.user
    admin = isAdmin(user)

    if admin == None:
        return

    establishments = admin.establishments

    return render(request, "a_index.html", context = {
            "user": user,
            "establishments" : establishments,
        }
    )