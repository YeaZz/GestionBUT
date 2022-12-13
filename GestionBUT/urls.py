from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("main.urls")),
    path('accounts/', include("accounts.urls")),
    path('student/', include("student.urls")),
    path('professor/', include("professor.urls")),
    path('administrator/', include("administrator.urls")),
]

urlpatterns += staticfiles_urlpatterns()