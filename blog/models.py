from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class General_Post(models.Model):
    user = models.ForeignKey(User , on_delete = models.CASCADE)
    image = models.ImageField(blank = True  , null = True, upload_to = 'generalposts')
    title = models.CharField(max_length=400 , null = True , blank=True)
    content  = models.TextField(null=True , blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.id)

class Academic_Post(models.Model):
    user = models.ForeignKey(User , on_delete = models.CASCADE)
    image = models.ImageField(blank = True  , null = True, upload_to = 'academicposts')
    title = models.CharField(max_length=400 , null = True , blank=True)
    content  = models.TextField(null=True , blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.id)
