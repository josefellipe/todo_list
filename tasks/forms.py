from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    description = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Write New Task',
            'class': 'form-control'
        })
    )

    class Meta:
        model = Task
        fields = ['description', 'completed']


class UpdateTaskForm(forms.ModelForm):
    description = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Update the task here',
            'class': 'form-control'
        })
    )

    class Meta:
        model = Task
        fields = ['description', 'completed']