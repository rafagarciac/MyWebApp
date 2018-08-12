from django.contrib import admin
from .models import Mycv, Experience, Education

# Register your models here.
admin.site.register(Mycv)
admin.site.register(Experience)
admin.site.register(Education)
