from django.shortcuts import render, redirect 

from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
from django.contrib.auth import login as user_login, logout as user_logout


from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login(request):
    user = request.user
    if user.is_authenticated:
        return redirect("main:index")
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            user_login(request, user)
            return redirect("main:index")
    else:
        form = AuthenticationForm()

    return render(request,
    "login.html",
    context = {
            "form": form
        }
    )

def logout(request):
    if request.method == "POST":
        user_logout(request)
        return redirect("login")

def profile(request):
    user = request.user
    if not user.is_authenticated:
        return redirect("login")
    return render(request, "profile.html")
