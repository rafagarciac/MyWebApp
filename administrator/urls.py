from django.conf.urls import url
from django.views.generic import RedirectView
from . import views

app_name = 'administrator'

urlpatterns = [
    #Regular Expression r'regularExprsHere'
    # /blog/
    url(r'^$', views.loginindex, name='loginindex'),
    url(r'blog', views.viewlogin, name='viewlogin'),
    url(r'aboutme', views.aboutme, name='aboutme'),
    url(r'logout', views.viewlogout, name='viewlogout'),
    url(r'^remove/(?P<idpost>[0-9]+)', views.blogremove, name='blogremove'),
    url(r'add', views.blognew, name='blognew'),
    url(r'^edit/(?P<idpost>[0-9]+)', views.blogedit, name='blogedit'),
    url(r'^savepost/(?P<idpost>[0-9]+)', views.savepost, name='savepost'),
    url(r'^saveme/(?P<id>[0-9]+)', views.saveaboutme, name='saveaboutme'),
]