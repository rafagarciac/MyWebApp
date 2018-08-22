
from django.shortcuts import render, get_object_or_404, get_list_or_404
# Import generic views
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Import Forms
from administrator.forms import ExperienceForm, EducationForm, ResumeForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.shortcuts import render
import time
# Import Models 
from blog.models import Post
from aboutme.models import Me
from cv.models import Mycv, Experience, Education

##########################################  L O G I N // L O G O U T   S E C T I O N #####################################
def loginindex (request):
    if 'username' not in request.session:
        return render(request, 'administrator/login/index.html', context=None, content_type=None, status=None, using=None)
    else:
        all_posts = get_list_or_404(Post.objects.all())
        context = {'posts': all_posts}
        return render(request, 'administrator/blog/index.html', context=context, content_type=None, status=None, using=None)


def viewlogout (request):
    #   Clear Session
    del request.session['username']
    del request.session['password']
    return render(request, 'administrator/login/index.html', context=None, content_type=None, status=None, using=None)


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
        return render(request, 'administrator/blog/index.html', context=context, content_type=None, status=None, using=None)
    else:
        # Return an 'invalid login' error message.
        return render(request, 'administrator/login/index.html', context={'loginfail': True}, content_type=None, status=None, using=None)

##########################################  B L O G    S E C T I O N #####################################

def blog_update (request, idpost):
    print("Method: " + request.method)
    print("Value: " + request.content_type)
    print("Path: " + request.path)
    print("IdPost: " + idpost)
    #post = Post.objects.get(pk=idpost)
    try:
        post = get_object_or_404(Post, pk = idpost)
    except (KeyError, Post.DoesNotExist):
        return render( request, 'administrator/blog/blog_form.html', {
            'Post': post,
            'error_message': "You didn't save a Valid Post",
            })
    else:
        return render(request, 'administrator/blog/blog_form.html', context={'Post': post}, content_type=None, status=None, using=None)

def savepost (request, idpost):
    try:
        post = Post.objects.get(pk=idpost)
    except (KeyError, Post.DoesNotExist):
        return render( request, 'administrator/blog/index.html', {
            'Post': post,
            'error_message': "You didn't save a Valid Post",
            })
    else:
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.textcontent = request.POST['textcontent']
        post.tags = request.POST['tags']
        post.section = request.POST['section']
        post.author = request.POST['author']
        if request.POST['date'] == "" or request.POST['date'] is None:
            #Current Date   Format: yyyy-mm-dd
            post.date = time.strftime("%Y-%m-%d")
        else:
            post.date = request.POST['date']
        post.save()
        # Redirect to List of Blogs
        all_posts = get_list_or_404(Post.objects.all())
        context = {'posts': all_posts}
        return render(request, 'administrator/blog/index.html', context=context, content_type=None, status=None, using=None)
        #Redirect to the same Post
        #return render(request, 'administrator/blog_form.html', {'Post': post})

def blog_delete (request, idpost):
    try:
        post = get_object_or_404(Post, pk = idpost)
        post.delete()
    except (KeyError, Post.DoesNotExist):
        return render( request, 'administrator/blog/blog_form.html', {
            'Post': post,
            'error_message': "You didn't save a Valid Post",
            })
    else:
        all_posts = get_list_or_404(Post.objects.all())
        context = {'posts': all_posts}
        return render(request, 'administrator/blog/index.html', context=context, content_type=None, status=None, using=None)

def blog_create (request):
    post = Post()
    post.date = time.strftime("%Y-%m-%d")
    post.tags = ''
    post.save()
    return render(request, 'administrator/blog/blog_form.html', context={'Post': post}, content_type=None, status=None, using=None)

##########################################  A B O U T   M E    S E C T I O N #####################################
def aboutme(request):
    me = get_object_or_404(Me, pk = 1)
    context = {'Me': me}
    return render(request, 'administrator/aboutme/index.html', context=context, content_type=None, status=None, using=None)

def saveaboutme(request, id):
    try:
        me = Me.objects.get(pk=id)
    except (KeyError, Me.DoesNotExist):
        return render( request, 'administrator/aboutme/index.html', {
            'Post': me,
            'error_message': "You didn't save a Valid AboutMe",
            })
    else:
        me.name = request.POST['name']
        me.title = request.POST['title']
        me.location = request.POST['location']
        me.bio = request.POST['bio']
        me.tags = request.POST['tags']
        me.work = request.POST['work']
        me.education = request.POST['education']
        me.twitter_url = request.POST['twitter_url']    
        me.linkedin_url = request.POST['linkedin_url']  
        me.github_url = request.POST['github_url']  
        me.email = request.POST['email']
        me.save()
        context = {'Me': me}
        return render(request, 'administrator/aboutme/index.html', context=context, content_type=None, status=None, using=None)



##########################################   C V // E X P E R I E N C E   S E C T I O N #####################################
class ExperienceIndexView(generic.ListView):
    template_name = "administrator/cv/experience/index.html"
    context_object_name = "experiences"

    def get_queryset(self):
        # cv = Mycv.objects.get(id=Mycv.DEFAULT_ID_CV)
        return Experience.objects.all().order_by('order')

class ExperienceDetailView(generic.DetailView):
    model = Experience
    template_name='administrator/cv/experience/detail.html'
    context_object_name = 'experience'

class ExperienceCreate(CreateView):
    model = Experience
    form_class = ExperienceForm
    template_name = 'administrator/cv/experience/experience_form.html'

class ExperienceUpdate(UpdateView):
    model = Experience
    form_class = ExperienceForm
    template_name = 'administrator/cv/experience/experience_form.html'
    
class ExperienceDelete(DeleteView):
    model = Experience
    success_url = reverse_lazy('administrator:experience_index')

##########################################   C V // E X P E R I E N C E   S E C T I O N #####################################

class EducationIndexView(generic.ListView):
    template_name = "administrator/cv/education/index.html"
    context_object_name = "educations"

    def get_queryset(self):
        # cv = Mycv.objects.get(id=Mycv.DEFAULT_ID_CV)
        return Education.objects.all().order_by('order')

class EducationDetailView(generic.DetailView):
    model = Education
    template_name='administrator/cv/education/detail.html'
    context_object_name = 'education'

class EducationCreate(CreateView):
    model = Education
    form_class = EducationForm
    template_name = 'administrator/cv/education/education_form.html'

class EducationUpdate(UpdateView):
    model = Education
    form_class = EducationForm
    template_name = 'administrator/cv/education/education_form.html'
    
class EducationDelete(DeleteView):
    model = Education
    success_url = reverse_lazy('administrator:education_index')

##########################################   C V // R E S U M E   S E C T I O N #####################################

class ResumeIndexView(generic.ListView):
    template_name = "administrator/cv/resume/index.html"
    context_object_name = "resumes"

    def get_queryset(self):
        # cv = Mycv.objects.get(id=Mycv.DEFAULT_ID_CV)
        return Mycv.objects.all()

class ResumeDetailView(generic.DetailView):
    model = Mycv
    template_name='administrator/cv/resume/detail.html'
    context_object_name = 'Resume'

class ResumeCreate(CreateView):
    model = Mycv
    form_class = ResumeForm
    template_name = 'administrator/cv/resume/resume_form.html'

class ResumeUpdate(UpdateView):
    model = Mycv
    form_class = ResumeForm
    template_name = 'administrator/cv/resume/resume_form.html'
    
class ResumeDelete(DeleteView):
    model = Mycv
    success_url = reverse_lazy('administrator:resume_index')

def displayChange(request, id):
    # Update all cv to Display = False and then put the select cv to display = True !
    for cv in Mycv.objects.all():
        cv.display = False
        cv.save()
    try:
        resume = get_object_or_404(Mycv, id = id)
    except (KeyError, Post.DoesNotExist):
        return render( request, 'administrator/cv/resume/index.html', {
            'resumes':  Mycv.objects.all(),
            'error_message': "Failes to update the ",
            })
    else:
        resume.display = True
        resume.save()
        return render(request, 'administrator/cv/resume/index.html', context={'resumes': Mycv.objects.all()}, content_type=None, status=None, using=None)