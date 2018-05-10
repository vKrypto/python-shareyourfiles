from django.shortcuts import render ,redirect
from .models import info ,Cred ,Employ_info ,upload
from .forms import Form1 ,Form3 ,Form4
from django.http import HttpResponse
from random import randint
from zerosms import sms
def generate_otp():
   return randint(10000 ,999999)
def clear_session():
   del request.session['ph']
   del request.session['email']
def send_otp_ph(recv,otp):
   user=9452855796
   paswd='K6546W'
   msg="otp is " + str(otp)
   sms(phno=user , passwd=paswd , message =msg , receivernum=recv)

def profile_pic(request):
   if request.method=='POST' and request.session['ph']:
      if Cred.objects.filter(ph=request.session['ph'] , signup_state=4):
         pic=Choose_pic(request.files)
         if pic.is_valid():
           basic= info.objects.get(ph='ph') 
           basic.picture= form.cleaned_data['pic']
           basic.save()
           return HttpResponse('profile_pic updated successfullly..')
   else:
      return render(request , 'signup/choosepic.html')

def signup1(request):
   if request.method=='POST':
      form = Form1(request.POST)
      if form.is_valid():
         basic=info()
         basic.fname =form.cleaned_data["fname"]
         basic.lname = form.cleaned_data["lname"]
         basic.email = form.cleaned_data["email"]
         basic.ph = form.cleaned_data["ph"]
         request.session['ph']=basic.ph
         request.session['email']=basic.email
         cred=Cred()
         cred.otp=0
         cred.reset=0
         cred.ph=basic.ph
         basic.save()
         cred.signup_state= 1
         cred.active =1
         cred.save()
         return redirect('/signup2') 
      else:
         return HttpResponse ('there is model (database related error)')
   else :
      return  render(request , 'signup/signup1/basic.html')


def signup2(request):
   if request.method=='POST' :
      mail=request.session['email']
      ph=request.session['ph']
      if request.POST.get('verify',False)=='ph':
         otp=generate_otp()
         mail=request.session['email']
         ph=request.session['ph']
         send_otp_ph( ph,otp)
         cred=Cred.objects.get(ph=ph)
         cred.otp=otp
         cred.save()
         return render(request , 'signup/signup2/confirmotp.html' ,{'phone' :ph , 'mail':mail})
      if request.POST['otp']:
         if Cred.objects.filter(ph=request.session['ph'], otp=request.POST['otp']).exists():
            cred=Cred.objects.get(ph=ph)
            cred.otp=0
            cred.signup_state=2
            cred.save()
            return redirect('/signup3')
         else:
            return HttpResponse('otp verification failed...')
   else :
      if request.session['ph'] :
         ph=request.session['ph']
         user= Cred.objects.get(ph=ph)
         if user.signup_state==1:
            return render(request , 'signup/signup2/verification.html' ,{'phone':ph , 'email':request.session['email']})
         else :
            return redirect('/signup1')
      else :
         return redirect('/signup1')


def signup3(request):
   if request.method=='POST':
      ph= request.session['ph']
      form = Form3(request.POST)
      if form.is_valid():
         emp=Employ_info()
         emp.ph =ph
         emp.desig= form.cleaned_data["desig"]
         emp.org= form.cleaned_data["org"]
         cred=Cred.objects.get( ph=ph )
         cred.signup_state= 3
         cred.active =1
         cred.save()
         return redirect('/signup4')
      else:
         return redirect('/signup3')
   else :
      if request.session['ph']:
         ph=request.session['ph']
         user= Cred.objects.get(ph=ph)
         state=user.signup_state
         if state != 2 :
            url='/signup'+ str(state)
            return redirect (url)
         else :
             return render(request ,'signup/signup3/employ.html')
      else :
         del request.session['ph']
         del request.session['email']
         return redirect('/signup1')


def signup4(request):
   if request.method=='POST':
      ph= request.session['ph']
      form = Form4(request.POST )
      if form.is_valid():
         user=Cred.objects.get(ph=ph)
         user.passw = form.cleaned_data["passwd"]
         del request.session['ph']
         del request.session['email']
         passw = user.passw
         user.signup_state= 4
         user.save()
         return render(request , 'signup/signup4/success.html' ,{'ph':ph , 'passw' : passw})
      else:
         return redirect('/signup4')
   else :
      if request.session['ph']:
         ph=request.session['ph']
         user= Cred.objects.get(ph=ph)
         state=user.signup_state
         if state !=3 :
            url='/signup'+ str(state)
            return redirect (url)
         else :
             return render(request ,'signup/signup4/choosepass.html')
      else :
         return redirect('/signup1')