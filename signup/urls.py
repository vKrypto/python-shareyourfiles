from django.conf.urls import url  
from . import views

urlpatterns = [
  url(r'^1$',views.signup1 ,name='signup1'),
  url(r'^2$',views.signup2 ,name='signup'),
  url(r'^3$',views.signup3 ,name='signup'),
  url(r'^4$',views.signup4 ,name='signup')
]
