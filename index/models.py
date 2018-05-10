from django.db import models

class Profile(models.Model):
   name = models.CharField(max_length = 50)
   picture = models.ImageField(upload_to = 'pictures')
   class Meta:
      db_table = "profile"

class basic_signup(models.Model):
   name=models.CharField(max_length=100)
   dob= models.IntegerField()
   email=models.CharField(max_length=100)
   ph=models.IntegerField()
   class Meta : 
      db_table='basic_signup'