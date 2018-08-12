from django.conf.urls import url
from django.views.generic import RedirectView
from . import views

app_name = 'cv'

urlpatterns = [
    #Regular Expression r'regularExprsHere'
    # url(r'^$', views.index, name='index'),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^experience/(?P<pk>[0-9]+)/$', views.ExperienceDetailView.as_view(), name='experience_detail'),
    url(r'^experience/add/$', views.ExperienceCreate.as_view(), name='experience_create'),
    url(r'^education/(?P<pk>[0-9]+)/$', views.EducationDetailView.as_view(), name='education_detail'),
    
]