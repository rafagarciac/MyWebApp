from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Post

# Create your views here.
def index (request):
    all_posts = Post.objects.all()
    context={'all_posts': all_posts}
    return render(request, 'blog/index.html',
                context,
                content_type=None,
                status=None,
                using=None)
    
def blogdetail (request, idpost):
    print("Method: " + request.method)
    print("Value: " + request.content_type)
    print("Path: " + request.path)
    print("IdPost: " + idpost)
    try: 
        post = Post.objects.get(pk=idpost)
    except Post.DoesnotExist:
        raise Http404("Post Does not Exist")
    return render(request, 'blog/blogdetail.html', 
                context={'Post': post}, 
                content_type=None, 
                status=None, 
                using=None)