from django import forms
from .models import UserRegistrationdb

class userForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = UserRegistrationdb
        fields = '__all__'

class optionForm(forms.ModelForm):
    class Meta:
        model = UserRegistrationdb
        fields = [
            'userid'
        ]

class updateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = UserRegistrationdb
        fields = '__all__'
