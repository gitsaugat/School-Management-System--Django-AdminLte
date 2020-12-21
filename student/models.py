from django.db import models
from django.utils import timezone
# Create your models here.

GENDER = (
    ('M' , 'male'),
    ('F' , 'female'),
    ('O' , 'other')
)

MAX_GRADE = 10

class Students(models.Model):
    image = models.ImageField(default = "default.png" , upload_to = 'student_profile_picture')
    fname = models.CharField(max_length=200 , null = True , blank=True)
    lname = models.CharField(max_length=200 , null = True , blank=True)
    fathername = models.CharField(max_length=300 , null = True , blank=True)
    mothername = models.CharField(max_length=200 , null = True , blank=True)
    class_of = models.IntegerField(  default =timezone.now().year )
    admitted_to = models.IntegerField( default= 1)
    section = models.CharField(max_length=2 , null = True  , blank = True)
    date_added = models.DateTimeField(auto_now_add=True)
    gender = models.CharField(choices=GENDER , max_length=10 , null = True , blank=True)
    phone_number = models.IntegerField(null = True , blank=True)
    student_email = models.EmailField(null = True , blank=True)
    def __str__(self):
        return str(self.id)

    @property 
    def returnClass(self):
        return str((timezone.now().year - self.class_of) + self.admitted_to)



