from django.conf.urls import url, include
from django.views.generic import RedirectView
from . import views

app_name = 'administrator'

urlpatterns = [
    #Regular Expression r'regularExprsHere'
    # /login/
    url(r'^$', views.loginindex, name='loginindex'),
    url(r'^blog/$', views.viewlogin, name='viewlogin'),
    # Not override the logout url.
    url(r'^log_out/$', views.viewlogout, name='viewlogout'),
    # /blog/
    url(r'^remove/(?P<idpost>[0-9]+)', views.blog_delete, name='blog_delete'),
    url(r'^blog/add/$', views.blog_create, name='blog_create'),
    url(r'^blog/edit/(?P<idpost>[0-9]+)/$', views.blog_update, name='blog_update'),
    url(r'^savepost/(?P<idpost>[0-9]+)', views.savepost, name='savepost'),
    # /aboutme/
    url(r'^aboutme/$', views.aboutme, name='aboutme'),
    url(r'^saveme/(?P<id>[0-9]+)', views.saveaboutme, name='saveaboutme'),  
    # /cv/resume
    url(r'^cv/$', views.ResumeIndexView.as_view(), name='resume_index'),
    url(r'^cv/resume/add/$', views.ResumeCreate.as_view(), name='resume_create'),
    url(r'^cv/resume/edit/(?P<pk>[0-9]+)/$', views.ResumeUpdate.as_view(), name='resume_update'),
    url(r'^cv/resume/(?P<pk>[0-9]+)/delete/$', views.ResumeDelete.as_view(), name='resume_delete'),
    url(r'^cv/resume/display_change/(?P<id>[0-9]+)/$', views.displayChange, name='display_change'),
    # /cv/experience
    url(r'^cv/experience/$', views.ExperienceIndexView.as_view(), name='experience_index'),
    url(r'^cv/experience/add/$', views.ExperienceCreate.as_view(), name='experience_create'),
    url(r'^cv/experience/edit/(?P<pk>[0-9]+)/$', views.ExperienceUpdate.as_view(), name='experience_update'),
    url(r'^cv/experience/(?P<pk>[0-9]+)/delete/$', views.ExperienceDelete.as_view(), name='experience_delete'),
    # /cv/education
    url(r'^cv/education/$', views.EducationIndexView.as_view(), name='education_index'),
    url(r'^cv/education/add/$', views.EducationCreate.as_view(), name='education_create'),
    url(r'^cv/education/edit/(?P<pk>[0-9]+)/$', views.EducationUpdate.as_view(), name='education_update'),
    url(r'^cv/education/(?P<pk>[0-9]+)/delete/$', views.EducationDelete.as_view(), name='education_delete'),
    # /skill/fields
    url(r'^skill/fields/$', views.FieldIndexView.as_view(), name='field_index'),
    url(r'^skill/fields/add/$', views.FieldCreate.as_view(), name='field_create'),
    url(r'^skill/fields/edit/(?P<pk>[0-9]+)/$', views.FieldUpdate.as_view(), name='field_update'),
    url(r'^skill/fields/(?P<pk>[0-9]+)/delete/$', views.FieldDelete.as_view(), name='field_delete'),
    # /skill/skills
    url(r'^skill/skills/$', views.SkillIndexView.as_view(), name='skill_index'),
    url(r'^skill/skills/add/$', views.SkillCreate.as_view(), name='skill_create'),
    url(r'^skill/skills/edit/(?P<pk>[0-9]+)/$', views.SkillUpdate.as_view(), name='skill_update'),
    url(r'^skill/skills/(?P<pk>[0-9]+)/delete/$', views.SkillDelete.as_view(), name='skill_delete'),
    
]