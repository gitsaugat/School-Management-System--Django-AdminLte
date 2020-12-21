from django import forms 
from .models import Admin_Staff
class AdminStaffCreationForm(forms.ModelForm):
    class Meta:
        model = Admin_Staff 
        fields = [
            'image',
            'fname',
            'lname',
            'age',
            'fathername',
            'mothername',
            'gender',
            'phone_number',
            'post',
            'email',
            'address',
            'maritual_status',
            'salary'
        ]