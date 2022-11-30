from django.shortcuts import render

def index(request):
    user = request.user
    return render(request, "content.html", context={"user": user})
