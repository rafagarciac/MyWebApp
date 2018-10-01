from django.conf.urls import url, include
from . import views

app_name = 'skills'

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^$', views.IndexView.as_view(), name='index'),
]