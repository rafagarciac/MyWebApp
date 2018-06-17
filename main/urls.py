from django.conf.urls import url
from . import views

urlpatterns = [
    #Regular Expression r'regularExprsHere'
    url(r'^$', views.index, name='index'),
]