from django import forms
from myapp.models import category,job

class Loginform(forms.Form):
    username=forms.CharField()
    password=forms.CharField()

class Categoryform(forms.ModelForm):
    class Meta:
        model=category
        fields=['name']

class Jobform(forms.ModelForm):
    class Meta:
        model=job
        fields='__all__'