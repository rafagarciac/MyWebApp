from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
# Create your views here.
'''
def index (request):
    return HttpResponse("<h1> Hello World! </h1>")
'''
def index (request):
    return render(request, 'main/index.html', context=None, content_type=None, status=None, using=None)
    
def viewlogin(request):
    sign = request.POST['sign']
    if sign == "signout":
        request.session.clear()
        return render(request, 'main/index.html', context=None, content_type=None, status=None, using=None)
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            request.session.username = username
            # Redirect to a success page.
            return render(request, 'main/index.html', context=None, content_type=None, status=None, using=None)
        else:
            # Return an 'invalid login' error message.
            return render(request, 'main/index.html', context=None, content_type=None, status=None, using=None)

def viewlogout(request):
    return render(request, 'main/index.html', context=None, content_type=None, status=None, using=None)