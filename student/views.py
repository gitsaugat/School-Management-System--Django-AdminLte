from django.shortcuts import render,redirect
from django.http import HttpResponse 
from .forms import AddStudentForm
from .models import Students
# Create your views here.


def students(request):
    return render(request , "student/students.html") 

def add_student(request):
    if request.method == "POST":
        form = AddStudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    form = AddStudentForm()

    context = {
        'form'  :form
    }
    return render(request , 'student/add.html' ,context)

def edit_student(request):
    context = {
        'students':Students.objects.all()
    }
    return render(request , 'student/edit.html' , context)

def edit_student_info(request , pk):
    student =  Students.objects.filter(pk = pk).first()
    if request.method == "POST":
        editform = AddStudentForm(
            request.POST , request.FILES , instance=student
        )
        if editform.is_valid():
            editform.save()
            return redirect('/edit/students')
    editform = AddStudentForm(
        instance=student
    )
    context = {
        'form'  : editform 
    }
    return render(request ,'student/editpage.html' , context )


def delete_student(request , pk):
    obj = Students.objects.filter(pk = pk).first()
    if request.method == "POST":
        obj.delete()
        return redirect('/edit/students')

    return render(request , 'student/confirm_delete.html')