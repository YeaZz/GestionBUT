from django.urls import path
from accounts.views import *
from django.contrib.auth import views

#app_name = 'accounts'

urlpatterns = [
    path('login/', login, name="login"),
    path('logout/', logout, name="logout"),
    path('profile/', profile, name="profile"),
    path('password_reset/', views.PasswordResetView.as_view(), name="password_reset"),
    path('password_reset/done/', views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('password_reset/reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('password_reset/reset/done/', views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]