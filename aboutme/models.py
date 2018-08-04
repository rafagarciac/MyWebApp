from django.db import models
import os

def get_image_path(instance, filename):
    return os.path.join(filename)

# Create your models here.
class Me(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=500)
    location = models.CharField(max_length=250)
    bio = models.TextField() 
    tags = models.TextField(default="''")
    work = models.CharField(max_length=500)
    education = models.CharField(max_length=500)
    twitter_url = models.CharField(max_length=500, default="https://twitter.com")
    linkedin_url = models.CharField(max_length=500, default="https://www.linkedin.com")
    email = models.CharField(max_length=500, default="profile")
    github_url = models.CharField(max_length=500, default="https://github.com")
    profileimage = models.ImageField(upload_to=get_image_path, blank=True, null=True)

    def __str__(self):
        return self.name + " // " + self.location + " // " + self.work
    
