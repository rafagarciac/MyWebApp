from django.conf.urls import url
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    #Regular Expression r'regularExprsHere'
    url(r'^$', views.index, name='index'),
    url(r'^favicon\.ico$',RedirectView.as_view(url='/static/admin/img/favicon.ico')),
]