from django.db import models
import os

def get_image_path(instance, filename):
    return os.path.join(filename)

# Create your models here.
class Post(models.Model):
    idpost = models.AutoField(primary_key=True)
    title = models.CharField(max_length=300)
    content = models.TextField()
    textcontent = models.TextField(default="Some text")
    author = models.CharField(max_length=50, default="Rafael García")
    section = models.CharField(max_length=50, default="General")
    tags = models.TextField(default="general") #IT|Components|OpenSource|Software|School
    image = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    date = models.DateField()

    def __str__(self):
        return self.idpost.__str__() + ". " + self.title + " (" + self.date.__str__() + ")"
        #return "\n ID: " + self.idpost.__str__() + "\n Titulo: " + self.title + "\n Contenido: " + self.content + "\n Fecha de Publicación: " + self.date.__str__() + "\n"

    def tags_as_list(self):
        return self.tags.replace("'", '').split(',')