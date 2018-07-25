from django.conf.urls import url
from django.views.generic import RedirectView
from . import views

app_name = 'administrator'

urlpatterns = [
    #Regular Expression r'regularExprsHere'
    # /blog/
    url(r'^$', views.loginindex, name='loginindex'),
    url(r'blog', views.viewlogin, name='viewlogin'),
    url(r'logout', views.viewlogout, name='viewlogout'),
    url(r'^remove/(?P<idpost>[0-9]+)', views.blogremove, name='blogremove'),
    url(r'add', views.blognew, name='blognew'),
    url(r'^edit/(?P<idpost>[0-9]+)', views.blogedit, name='blogedit'),
    url(r'^(?P<idpost>[0-9]+)', views.save, name='save'),
]