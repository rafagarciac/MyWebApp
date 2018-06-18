from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
'''
def index (request):
    return HttpResponse("<h1> Hello World! </h1>")
'''
def index (request):
    return render(request, 'main/index.html', context=None, content_type=None, status=None, using=None)
    
