from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include('mainApp.urls')),
    url(r'^education/', include('mainApp.urls')),
]
