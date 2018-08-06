from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index (request):
    return render(request, 'cv/index.html', context=None, content_type=None, status=None, using=None)
    