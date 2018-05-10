
from django.conf import settings
from django.conf.urls.static import static


from django.contrib import admin
from django.urls import path
from django.conf.urls import url  , include

from uploads.core import views

urlpatterns = [
    
	url(r'^uploads$', views.home, name='home'),
    url(r'^uploads/simple/$', views.simple_upload, name='simple_upload'),
    url(r'^uploads/form/$', views.model_form_upload, name='model_form_upload'),

    path('admin/', admin.site.urls),
    url(r'^', include('index.urls')),
    url(r'^signup', include('signup.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
