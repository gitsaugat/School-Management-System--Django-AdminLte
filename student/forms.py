from django import forms 
from student.models import Students

class AddStudentForm(forms.ModelForm):

    class Meta:

        model = Students
        fields = [
            'image',
            'fname',
            'lname',
            'fathername',
            'mothername',
            'class_of',
            'admitted_to',
            'section',
            'gender',
            'phone_number',
            'student_email'
        ]
