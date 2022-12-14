from django.shortcuts import render, redirect 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main:index')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('accounts:login')

def profile_view(request):
    return render(request, "profile.html")