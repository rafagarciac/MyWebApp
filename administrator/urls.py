from django.conf.urls import url, include
from django.views.generic import RedirectView
from . import views

app_name = 'administrator'

urlpatterns = [
    #Regular Expression r'regularExprsHere'
    # /login/
    url(r'^$', views.loginindex, name='loginindex'),
    url(r'^blog/$', views.viewlogin, name='viewlogin'),
    url(r'^logout/$', views.viewlogout, name='viewlogout'),
    # /blog/
    url(r'^remove/(?P<idpost>[0-9]+)', views.blog_delete, name='blog_delete'),
    url(r'^blog/add/$', views.blog_create, name='blog_create'),
    url(r'^blog/edit/(?P<idpost>[0-9]+)/$', views.blog_update, name='blog_update'),
    url(r'^savepost/(?P<idpost>[0-9]+)', views.savepost, name='savepost'),
    # /aboutme/
    url(r'^aboutme/$', views.aboutme, name='aboutme'),
    url(r'^saveme/(?P<id>[0-9]+)', views.saveaboutme, name='saveaboutme'),  
    # /cv/experience
    url(r'^cv/experience/$', views.ExperienceIndexView.as_view(), name='experience_index'),
    url(r'^cv/experience/add/$', views.ExperienceCreate.as_view(), name='experience_create'),
    url(r'^cv/experience/edit/(?P<pk>[0-9]+)/$', views.ExperienceUpdate.as_view(), name='experience_update'),
    url(r'^cv/experience/(?P<pk>[0-9]+)/delete/$', views.ExperienceDelete.as_view(), name='experience_delete'),
    # /cv/education
]