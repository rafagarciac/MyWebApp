from django.shortcuts import render, get_object_or_404, get_list_or_404
from aboutme.models import Me
# Create your views here.
def index (request):
    #all_posts = Post.objects.all()
    #all_posts = get_list_or_404(Post.objects.all())
    #context={'all_posts': all_posts}
    me = get_object_or_404(Me, pk = 1)
    context = {'Me': me}
    return render(request, 'aboutme/index.html',
                context=context,
                content_type=None,
                status=None,
                using=None)
