from django import forms
from django.forms import ModelForm
from .models import Job

class JobSelectForm(forms.Form):
    jobs = forms.ModelMultipleChoiceField(queryset=Job.objects.all(),widget=forms.CheckboxSelectMultiple)