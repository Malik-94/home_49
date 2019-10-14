from django import forms
from webapp.models import Status, Type, Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ['created_at']


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['statuses']


class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = ['types']


class SimpleSearchForm(forms.Form):

    search = forms.CharField(max_length=100, required=False, label="Найти")

