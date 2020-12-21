from django import forms 
from .models import Teacher
class TeacherCreationForm(forms.ModelForm):
    class Meta : 
        model = Teacher 
        fields = [
            'image',
            'fname',
            'lname',
            'age',
            'fathername',
            'mothername',
            'level',
            'subject',
            'gender',
            'phone_number',
            'email',
            'address',
            'maritual_status',
            'salary'
        ]