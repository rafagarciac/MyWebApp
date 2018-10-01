from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from .models import Field, Skill

# Create your views here.
class IndexView(generic.ListView):
    template_name="skills/index.html"
    context_object_name = "skills_list"

    def get_queryset(self):
        return Skill.getSkills('order') # Skill.objects.all().order_by('order') -> Pass the value for want we order.

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['data_labels'] = Field.getNameFields()
        context['data_chart'] = Field.getArrayByFieldsMath()
        context['data_colors'] = Field.getColorsByField()
        context['data_hover_colors'] = Field.getHoverColorsByField()
        return context