from django.conf.urls import url 
from . import views
urlpatterns = [
url(r'^$' , views.index ,name='index'),
  url(r'^logout$' , views.logout, name = 'logout'),
  url(r'^upload$' , views.upload, name = 'upload'),
  url(r'^about$' , views.about, name = 'about'),

]
