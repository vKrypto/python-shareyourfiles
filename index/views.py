from django.shortcuts import render ,redirect
from .forms import LoginForm
from django.http import HttpResponse
from signup.models import Cred ,info
from .models import Profile

from uploads.core.models import Document

from uploads.core.forms import DocumentForm 




def logout(request):
   try:
      del request.session['username']
      del request.session['userid']
   except:
      pass
   return redirect('/')


def index(request):
   if request.method == 'POST' :  
      if request.POST.get('userid',False):
         MyLoginForm = LoginForm(request.POST)      
         if MyLoginForm.is_valid() and Cred.objects.filter(ph=request.POST['userid']).exists() :
            userid = MyLoginForm.cleaned_data['userid']
            user=Cred.objects.get(ph= userid )
            if user.active :
               if not user.reset:
                  if user.signup_state == 4 :
                     return render( request ,'index/checkpass.html', {'userid':userid})
                  return redirect('/signup')
               return redirect('/signup')
            return HttpResponse('your account have been deactivated.')
         return HttpResponse (' form cred validation failed') 
      if request.POST.get('passwd',False):
         if Cred.objects.filter(ph=request.POST['id'], passw=request.POST['passwd']).exists():
            request.session['userid']= request.POST['id']
            basic=info.objects.get(ph= request.POST['id'])
            request.session['username']=basic.fname
            return render(request, 'index/home2.html', {'basic': basic })
         return HttpResponse('password is wrong .')
      if request.FILES and request.POST:
         if 'username' in request.session :
            basic=info.objects.get(ph= request.session['userid'])
            form=DocumentForm(request.POST ,request.FILES)
            if form.is_valid():
               form.save()
               documents = Document.objects.all()
               return render(request, 'index/home2.html', { 'documents': documents,'basic':basic })
           			
      return redirect('/')
   if request.method=='GET':
      if 'username' in request.session :
         basic=info.objects.get(ph= request.session['userid'])
         form = DocumentForm()
         return render(request ,'index/home2.html' ,{'form':form , "basic" :basic  })
      else :
         return render(request, 'index/index.html')
       
def about (reuest):
   return render(request , 'about.html')


def upload(request):
   if request.method == 'POST':
      form = DocumentForm(request.POST, request.FILES)
      if form.is_valid():
         form.save()
         basic=info.objects.get(ph= request.session['userid'])
         documents = Document.objects.all() 
         return render(request, 'index/home2.html', { 'documents': documents,'basic':basic })
   else:
      form = DocumentForm()
   return render(request, 'index/home2.html', {'form': form})