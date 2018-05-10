from django.db import models

class info(models.Model):
   fname= models.CharField(max_length = 100)
   email = models.CharField(max_length = 100)
   lname = models.CharField(max_length =100)
   ph = models.IntegerField()
   picture = models.ImageField(upload_to = 'profile_pics')

class Cred(models.Model):
   signup_state=models.IntegerField()
   ph=models.IntegerField()
   passw = models.CharField(max_length=50)
   reset=models.IntegerField()
   active= models.IntegerField()
   otp=models.IntegerField()

class Employ_info :
   desig= models.CharField(max_length=100)
   org= models.CharField(max_length=100)
   ph =models.IntegerField()


class upload(models.Model):
   no_files = models.IntegerField()
   ph = models.IntegerField()