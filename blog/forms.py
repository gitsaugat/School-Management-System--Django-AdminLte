from django import forms 
from .models import Academic_Post , General_Post


class AcademicPostCreationForm(forms.ModelForm):

    class Meta:
        model = Academic_Post
        fields = [
            'image',
            'title',
            'content'
        ]

class GeneralPostCreationForm(forms.ModelForm):

    class Meta:
        model = General_Post
        fields = [
            'image',
            'title',
            'content'
        ]