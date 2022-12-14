from django.urls import path, include
from accounts.views import *

app_name = 'accounts'

urlpatterns = [
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('profile/', profile_view, name="profile"),
]