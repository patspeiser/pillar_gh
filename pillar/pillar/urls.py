from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('orgs/', include('github.urls')),
    path('admin/', admin.site.urls),
]
