from django.shortcuts import render , redirect
from .forms import TeacherCreationForm 
from .models import Teacher
from django.db.models import Q
# Create your views here.


def teachers(request):

    context = {
        'teachers' : Teacher.objects.all()
    }

    return render(request , 'teachers/teachers.html' , context)

def create_teacher(request):

    if request.method == 'POST':
        form = TeacherCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/teachers')
    form = TeacherCreationForm()
    context = {
        'form' : form 
    }
    return render(request , 'teachers/create.html' ,context)



def edit_teachers_info(request , pk):
    teacher =  Teacher.objects.filter(pk = pk).first()
    if request.method == "POST":
        editform = TeacherCreationForm(
            request.POST , request.FILES , instance=teacher
        )
        if editform.is_valid():
            editform.save()
            return redirect('/edit/students')
    editform = TeacherCreationForm(
        instance=teacher
    )
    context = {
        'form'  : editform 
    }
    return render(request ,'teachers/EditTeacher.html' , context )



def delete_teacher(request , pk):
    obj = Teacher.objects.filter(pk = pk).first()
    if request.method == "POST":
        obj.delete()
        return redirect('/teachers')

    return render(request , 'teachers/confirm_delete.html')
