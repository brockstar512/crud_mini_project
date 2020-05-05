from django.conf.urls import url
from apps.authentication.views import RegistrationAPIView, LoginAPIView
urlpatterns = [
    url(r'^users/register/$', RegistrationAPIView.as_view(), name='register'),
    url(r'^users/login/$', LoginAPIView.as_view(), name='login'),

#then go to the mini_project url and add some things
]