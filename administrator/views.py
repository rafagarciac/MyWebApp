
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib.auth import authenticate, login
from django.shortcuts import render
import time
#Import Posts from blog Application for add, edit & remove Posts 
from blog.models import Post

# Create your views here.
def loginindex (request):
    if 'username' not in request.session:
        return render(request, 'administrator/loginindex.html', context=None, content_type=None, status=None, using=None)
    else:
        all_posts = get_list_or_404(Post.objects.all())
        context = {'posts': all_posts}
        return render(request, 'administrator/blog.html', context=context, content_type=None, status=None, using=None)


def viewlogout (request):
    #   Clear Session
    del request.session['username']
    del request.session['password']
    return render(request, 'administrator/loginindex.html', context=None, content_type=None, status=None, using=None)


def viewlogin(request):
    if 'username' not in request.session:
        username = request.POST['username']
        password = request.POST['password']
    else:
        username = request.session['username']
        password = request.session['password']
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        request.session['username'] = username
        request.session['password'] = password
        # Redirect to a success page.
        all_posts = get_list_or_404(Post.objects.all())
        context = {'posts': all_posts, 'loginfail': False}
        return render(request, 'administrator/blog.html', context=context, content_type=None, status=None, using=None)
    else:
        # Return an 'invalid login' error message.
        return render(request, 'administrator/loginindex.html', context={'loginfail': True}, content_type=None, status=None, using=None)


def blogedit (request, idpost):
    print("Method: " + request.method)
    print("Value: " + request.content_type)
    print("Path: " + request.path)
    print("IdPost: " + idpost)
    #post = Post.objects.get(pk=idpost)
    try:
        post = get_object_or_404(Post, pk = idpost)
    except (KeyError, Post.DoesNotExist):
        return render( request, 'administrator/blogdetailedit.html', {
            'Post': post,
            'error_message': "You didn't save a Valid Post",
            })
    else:
        return render(request, 'administrator/blogdetailedit.html', context={'Post': post}, content_type=None, status=None, using=None)

def save (request, idpost):
    try:
        post = Post.objects.get(pk=request.POST['idpost'])
    except (KeyError, Post.DoesNotExist):
        return render( request, 'administrator/blog.html', {
            'Post': post,
            'error_message': "You didn't save a Valid Post",
            })
    else:
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.textcontent = request.POST['textcontent']
        post.tags = request.POST['tags']
        post.section = request.POST['section']
        if request.POST['date'] == "" or request.POST['date'] is None:
            #Current Date   Format: yyyy-mm-dd
            post.date = time.strftime("%Y-%m-%d")
        else:
            post.date = request.POST['date']
        post.save()
        # Redirect to List of Blogs
        all_posts = get_list_or_404(Post.objects.all())
        context = {'posts': all_posts}
        return render(request, 'administrator/blog.html', context=context, content_type=None, status=None, using=None)
        #Redirect to the same Post
        #return render(request, 'administrator/blogdetailedit.html', {'Post': post})

def blogremove (request, idpost):
    try:
        post = get_object_or_404(Post, pk = idpost)
        post.delete()
    except (KeyError, Post.DoesNotExist):
        return render( request, 'blog/blogdetail.html', {
            'Post': post,
            'error_message': "You didn't save a Valid Post",
            })
    else:
        all_posts = get_list_or_404(Post.objects.all())
        context = {'posts': all_posts}
        return render(request, 'administrator/blog.html', context=context, content_type=None, status=None, using=None)

def blognew (request):
    post = Post()
    post.date = time.strftime("%Y-%m-%d")
    post.tags = ''
    post.save()
    return render(request, 'administrator/blogdetailedit.html', context={'Post': post}, content_type=None, status=None, using=None)
    
        