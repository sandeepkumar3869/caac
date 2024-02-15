from django.db import models
import datetime
import uuid
from django.contrib.auth.models import User

# Create your models here.
class bottomlevel(models.Model):
    taskid = models.UUIDField(auto_created =True,primary_key=True,default=uuid.uuid4)
    task_title = models.TextField(max_length=255,blank=False)
    task_description = models.TextField(null=True)
    task_created_on = models.DateTimeField(default=datetime.datetime.now())
    task_ccompleted_on = models.DateTimeField(blank=True,null=True)

# def __str__(self):
#     return self.task_tittle[:50]
class contactus(models.Model):
    name = models.CharField(max_length = 100)
    phone = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    message = models.TextField()
    date = models.DateField()

class Usertbl(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    name = models.CharField(max_length=255,default="DefaultName")
    last_name = models.CharField(max_length=255,null=True)

    def __str__(self):
        return self.email




