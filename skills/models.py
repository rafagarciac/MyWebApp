from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from colorfield.fields import ColorField
from operator import attrgetter
import os

def get_image_path(instance, filename):
    return os.path.join(filename)

# Create your models here.
class Field(models.Model):
    color = ColorField(default='#FF0000')
    name = models.CharField(max_length=200, blank=True, default="Field")
    FIELD_ID_DEFAULT = 1

    def get_absolute_url(self):
        return reverse('administrator:field_index')

    # Function that calculate the Total Percentage about Fields of all Skills
    # -------- Math Formula --------
    # Example -> 20% CSS + 80% HTML (Field: Design) -> 100% / SkillsNumberPerField -> (Result % * 100%) / FieldsNumber -> TOTAL   
    def getArrayByFieldsMath():
        parcialPercentages = []
        totalPercentages = []

        for field in Field.objects.all():
            subtotal = 0
            if len(field.skill_set.all()) > 0:
                for skill in field.skill_set.all():
                    subtotal += skill.percentage
                parcialPercentages.append(subtotal / len(field.skill_set.all()))

        total = sum(parcialPercentages[0:len(parcialPercentages)])
        for parcialPercentage in parcialPercentages: 
            totalPercentages.append(round(((parcialPercentage * 100) / total), 2))
            
        return totalPercentages


    # Return the Fields Colors Dinamically
    def getColorsByField():
        colorFields = []
        for field in Field.objects.all():
            colorFields.append(('rgba' + tuple(int(field.color.replace('#', '')[i:i+2], 16) for i in (0, 2 ,4)).__str__())[:-1] + ', 0.5)')
        return colorFields

    
    # Return the Fields Hover Colors Dinamically
    def getHoverColorsByField():
        hoverColorFields = []
        for field in Field.objects.all():
            hoverColorFields.append(('rgb' + tuple(int(field.color.replace('#', '')[i:i+2], 16) for i in (0, 2 ,4)).__str__()))
        return hoverColorFields

    # Return the names of the Fields Dinamically
    def getNameFields():
        namesFields = []
        for field in Field.objects.all():
            namesFields.append(field.name)

        return namesFields

    def __str__(self):
        return "{0}".format(self.name)


class Skill(models.Model):
    name = models.CharField(max_length=200, blank=True, default="Skill")
    percentage = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    image = models.ImageField(upload_to=get_image_path, blank=False, null=True)
    order = models.IntegerField(blank=True, unique=False, default=1)
    field = models.ForeignKey(Field, on_delete=models.CASCADE, default=Field.FIELD_ID_DEFAULT)

    def get_absolute_url(self):
        return reverse('administrator:skill_index')

    # Return the all skills include the color attribute referenced in Field Object ;)
    def getSkills(orderBy):
        from .models import Field
        skills = []
        
        for skill in Skill.objects.all():
            skill.color = Field.objects.get(id=skill.field.id).color
            skills.append(skill)

        return sorted(skills, key=attrgetter(orderBy))


    def __str__(self):
        return "{0} .- {1}% .- {2} -. {3}".format(self.name, self.percentage.__str__(), self.order.__str__(), self.field.name)