from django.db import models

# Create your models here.
class Post(models.Model):
    idpost = models.AutoField(primary_key=True)
    title = models.CharField(max_length=300)
    content = models.TextField()
    textcontent = models.TextField(default="Some text")
    date = models.DateField()

    def __str__(self):
        return self.idpost.__str__() + ". " + self.title + " (" + self.date.__str__() + ")"
        #return "\n ID: " + self.idpost.__str__() + "\n Titulo: " + self.title + "\n Contenido: " + self.content + "\n Fecha de Publicación: " + self.date.__str__() + "\n"
        
# class Profile
# class Comment