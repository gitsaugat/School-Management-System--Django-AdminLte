from django.db import models

# Create your models here.

GENDER = (
    ('M' , 'male'),
    ('F' , 'female'),
    ('O' , 'other')
)

STATUS = (
    ('M' , 'married'),
    ('U' , 'unmarried'),
)
class Admin_Staff(models.Model):
    image = models.ImageField(default = "default.png" , upload_to = 'admin')
    fname = models.CharField(max_length=200 , null = True , blank=True)
    lname = models.CharField(max_length=200 , null = True , blank=True)
    age   = models.IntegerField(null = True , blank=True)
    fathername = models.CharField(max_length=300 , null = True , blank=True)
    mothername = models.CharField(max_length=200 , null = True , blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    gender = models.CharField(choices=GENDER , max_length=10 , null = True , blank=True)
    phone_number = models.IntegerField(null = True , blank=True)
    post = models.CharField(max_length=300 , null = True , blank=True)
    email = models.EmailField(null = True , blank=True)
    address = models.CharField(max_length=300 , null = True , blank = True)
    maritual_status = models.CharField(choices = STATUS , blank= True , null = True , max_length=10)
    salary = models.IntegerField(null = True , blank = True)
    def __str__(self):
        return str(self.id)
