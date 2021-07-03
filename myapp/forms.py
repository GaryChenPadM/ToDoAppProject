from django import forms
from .models import ToDo

class TaskForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = "task" , "description" , "priority"
        