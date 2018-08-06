from django.conf.urls import url
from django.views.generic import RedirectView
from . import views

app_name = 'cv'

urlpatterns = [
    #Regular Expression r'regularExprsHere'
    url(r'^$', views.index, name='index'),
]