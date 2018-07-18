
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib.auth import authenticate, login
from django.shortcuts import render
#Import Posts from blog Application for add, edit & remove Posts 
from blog.models import Post

# Create your views here.
def loginindex (request):
    return render(request, 'administrator/loginindex.html',
                context=None,
                content_type=None,
                status=None,
                using=None)

def viewlogin(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        #request.session.username = username
        # Redirect to a success page.
        return render(request, 'administrator/blog.html', context=None, content_type=None, status=None, using=None)
    else:
        # Return an 'invalid login' error message.
        return render(request, 'administrator/loginindex.html', context=None, content_type=None, status=None, using=None)