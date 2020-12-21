from django.shortcuts import render , redirect
from .forms import AdminStaffCreationForm 
from .models import Admin_Staff
# Create your views here.


def adminstaffs(request):
    context = {
        'adminstaffs' : Admin_Staff.objects.all()
    }
    return render(request , 'administration/adminstaffs.html' , context)

def create_admin_staff(request):

    if request.method == 'POST':
        form = AdminStaffCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/adminstaffs')
    form = AdminStaffCreationForm()
    context = {
        'form' : form 
    }
    return render(request , 'administration/create.html' ,context)



def edit_adminstaff_info(request , pk):
    adminstaff =  Admin_Staff.objects.filter(pk = pk).first()
    if request.method == "POST":
        editform = AdminStaffCreationForm(
            request.POST , request.FILES , instance=adminstaff
        )
        if editform.is_valid():
            editform.save()
            return redirect('/adminstaffs')
    editform = AdminStaffCreationForm(
        instance=adminstaff
    )
    context = {
        'form'  : editform 
    }
    return render(request ,'administration/edit_staff.html' , context )



def delete_admin_staff(request , pk):
    obj = Admin_Staff.objects.filter(pk = pk).first()
    if request.method == "POST":
        obj.delete()
        return redirect('/adminstaffs')

    return render(request , 'administration/confirm_delete.html')
