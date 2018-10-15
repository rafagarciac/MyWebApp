from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
import os

from .models import File, Folder
# Create your views here.

def index (request):
    folders = Folder.getFoldersOrderByLevel()
    return render(request, 'cloudfiles/index.html', context={'folders': folders}, content_type=None, status=None, using=None)

def folderSystem(request, pathfolder):
    folders = Folder.objects.all()
    return render(request, 'cloudfiles/system.html', context={'folders': folders}, content_type=None, status=None, using=None)
