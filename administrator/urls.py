from django.conf.urls import url
from django.views.generic import RedirectView
from . import views

app_name = 'administrator'

urlpatterns = [
    #Regular Expression r'regularExprsHere'
    # /blog/
    url(r'^$', views.loginindex, name='loginindex'),
    url(r'blogedit', views.viewlogin, name='viewlogin'),
]