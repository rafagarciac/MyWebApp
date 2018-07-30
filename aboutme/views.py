from django.shortcuts import render, get_object_or_404, get_list_or_404

# Create your views here.

# Create your views here.
def index (request):
    #all_posts = Post.objects.all()
    #all_posts = get_list_or_404(Post.objects.all())
    #context={'all_posts': all_posts}
    return render(request, 'aboutme/index.html',
                context=None,
                content_type=None,
                status=None,
                using=None)
