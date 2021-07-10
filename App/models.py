from django.db import models

# Create your models here.
class Contact(models.Model):
   name = models.CharField(max_length=122, blank=True,null=True,default='enter')
   email= models.CharField(max_length=122, blank=True,null=True,default='enter')
   subject = models.CharField(max_length=122, blank=True,null=True,default='enter')
   message = models.CharField(max_length=12, blank=True,null=True,default='enter')


   def __str__(self):
      return self.name
