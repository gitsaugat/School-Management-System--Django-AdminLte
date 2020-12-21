from django.shortcuts import render , redirect
from .forms import ExtraWorkerCreationForm 
from .models import Extra_Worker
# Create your views here.

def extrastaffs(request):
    context = {
        'extraworkers' : Extra_Worker.objects.all()
    }
    return render(request , 'extraworkers/extraworkers.html' , context)

def create_extra_staff(request):

    if request.method == 'POST':
        form = ExtraWorkerCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/extraworkers')
    form = ExtraWorkerCreationForm()
    context = {
        'form' : form 
    }
    return render(request , 'extraworkers/create.html' ,context)



def edit_extra_staff(request , pk):
    extraworker =  Extra_Worker.objects.filter(pk = pk).first()
    if request.method == "POST":
        editform = ExtraWorkerCreationForm(
            request.POST , request.FILES , instance=extraworker
        )
        if editform.is_valid():
            editform.save()
            return redirect('/extraworkers')
    editform = ExtraWorkerCreationForm(
        instance=extraworker
    )
    context = {
        'form'  : editform 
    }
    return render(request ,'extraworkers/edit_staff.html' , context )

def delete_extra_staff(request , pk):
    obj = Extra_Worker.objects.filter(pk = pk).first()
    if request.method == "POST":
        obj.delete()
        return redirect('/extraworkers')

    return render(request , 'extraworkers/confirm_delete.html')
