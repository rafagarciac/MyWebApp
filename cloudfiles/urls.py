from django.conf.urls import url
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = "cloudfiles"

urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'<path:pathfolder>', views.folderSystem, name='folder_system'),
]