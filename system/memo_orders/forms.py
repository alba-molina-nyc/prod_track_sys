from django import forms
from .models import MemoOrder


class MemoOrderForm(forms.ModelForm):
    class Meta:
        model = MemoOrder
        fields = ['setter_fname', 'setter_lname', 'setter_email', 'note']