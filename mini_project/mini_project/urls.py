
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('apps.authentication.urls')),
    path('api/', include('apps.api.urls')),
]
#these paths are where I need a long in
#include(the urls from this file)

##python manage.py makemigrations
#python manage.py migrate
#python manage.py runserver