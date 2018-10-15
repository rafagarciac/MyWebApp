from django.db import models
from  datetime import date
from operator import attrgetter
import os

# Create your models here.
def filesImagePath(instance, filename):
    return os.path.join("images/" + filename)

def filesPath(instance, filename):
    # instance...
    return os.path.join(filename + "/main")

class Folder(models.Model):
    name = models.CharField(max_length=100, blank=True, default="Default Folder")
    path = models.CharField(max_length=1000, blank=True, default="main")                    # main/...
    parent = models.CharField(max_length=100, blank = True, default="main")  

    def getFoldersOrderByLevel():     
        # # Set the Folder levels for Organize in UI
        folders = Folder.objects.all()
        for folder in folders:
            folder.level = len(folder.path.split('/')) - 1

        folders = sorted(folders, key=attrgetter("level"))
        # max_level = Folder.objects.latest('level')

        # for i in range(max_level):
        #     folders = getFoldersByLevel(i)

        # for folder in Folder.objects.all():
        #     folders.append(getStructureFolder(folder.name, folder.level))
        return folders

    # Under Develop - TODO
    def getFoldersByLevel(levelFolder):
        foldersNewArray = []
        folders = Folder.objects.filter(level=levelFolder) 
        if len(folders) != 0:
            for folder in folders:
                foldersNewArray.append(folder)

            
class File(models.Model):
    TYPES_OF_FYLES = (
        ('img', 'Image'),
        ('video', 'Video'),
        ('music', 'Music'),
        ('doc', 'Document'),
        ('file', 'File'),
        # Add more in the future https://en.wikipedia.org/wiki/List_of_file_formats 
    )
    type = models.CharField(max_length=50, choices=TYPES_OF_FYLES, default='file')
    file = models.FileField(upload_to=filesPath, default=None)
    thumbnail = models.ImageField(upload_to=filesImagePath, blank=False, null=True)
    name = models.CharField(max_length=100, blank=True, default="Default File") 
    size = models.CharField(max_length=100, blank=True, default="0")                        # 50MB // 1,34 KB ... editable = False ?
    date = models.DateTimeField(auto_now=True, auto_now_add=False)      # editable=False and blank=True set.
    visible = models.BooleanField(default=True)
    encoding = models.CharField(max_length=100, blank=True, default="...")                  # Encoding -> png/doc/zip/mp4... NOT CHARACTER ENCONDING  
    path = models.CharField(max_length=1000, blank=True)                                    # .../.../...
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)