from django.shortcuts import render
from student.models import Students
from teachers.models import Teacher
from extraworkers.models import Extra_Worker
from administration.models import Admin_Staff as adminstaff
from blog.models import Academic_Post , General_Post
# Create your views here.

def dashboard(request):
    
    context = {
        'title'  :'Dashboard',
        'adminstaffs' : adminstaff.objects.all(),
        'noofstudents' : len(Students.objects.all()),
        'noofteachers' : len(Teacher.objects.all()),
        'noofextraworkers' : len(Extra_Worker.objects.all()),
        'noofadminstaff' :len(adminstaff.objects.all()),
        'teachers' : Teacher.objects.all(),
        'students' : Students.objects.all(),
        'extraworkers' : Extra_Worker.objects.all(),
        'academicpostslength' : len(Academic_Post.objects.all()),
        'generalpostslength' : len(General_Post.objects.all()),
        'totalstaff' : sum([
            len(adminstaff.objects.all()),
            len(Extra_Worker.objects.all()),
            len(Teacher.objects.all()),
        ]),
        'totalposts' : sum([
            len(Academic_Post.objects.all()),
            len(General_Post.objects.all())
        ])

    }
    return render(request , 'boards/dashboard.html' , context)


def _404(request):
    return render(request , 'boards/404.html')
