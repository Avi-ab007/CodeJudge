from django import forms
from django.contrib.auth.models import User
from .models import Problem


class ProblemForm(forms.ModelForm):

    class Meta:
        model = Problem
        fields = ['pname', 'pcode', 'pdesc', 'author', 'test_input', 'answer']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()
