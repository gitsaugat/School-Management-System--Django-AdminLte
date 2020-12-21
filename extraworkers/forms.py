from django import forms 
from .models import Extra_Worker
class ExtraWorkerCreationForm(forms.ModelForm):
    class Meta:
        model = Extra_Worker 
        fields = [
            'image',
            'fname',
            'lname',
            'age',
            'fathername',
            'mothername',
            'gender',
            'phone_number',
            'work',
            'email',
            'address',
            'maritual_status',
            'salary'
        ]