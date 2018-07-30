from django.conf.urls import url
from django.views.generic import RedirectView
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'aboutme'

urlpatterns = [
    #Regular Expression r'regularExprsHere'
    # /aboutme/
    url(r'^$', views.index, name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)