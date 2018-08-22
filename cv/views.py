from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse

from .models import Mycv, Experience, Education
# Create your views here.
class IndexView(generic.ListView):
    template_name = "cv/index.html"
    context_object_name = "experiences_list"

    def get_queryset(self):
        cv = Mycv.objects.get(display=True)
        return cv.experience_set.all().order_by('order') 
    
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        cv = Mycv.objects.get(display=True)
        context['educations_list'] = cv.education_set.all().order_by('order') 
        return context

class ExperienceDetailView(generic.DetailView):
    model = Experience
    template_name='cv/experience_detail.html'
    context_object_name = 'experience'

class EducationDetailView(generic.DetailView):
    model = Education
    template_name='cv/education_detail.html'
    context_object_name = 'education'

def index (request):
    return render(request, 'cv/index.html', context=None, content_type=None, status=None, using=None)
