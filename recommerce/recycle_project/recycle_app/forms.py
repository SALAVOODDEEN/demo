from django import forms
from django.contrib.auth.models import User
from django.core import validators
from recycle_app.models import UserProfileInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password=forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        all_clean_data = super().clean()
        pword=all_clean_data['password']
        cword=all_clean_data['confirm_password']

        if pword!=cword:
            raise forms.ValidationError('make sure confirm password must match password')



    class Meta():
        model = User
        fields = ('username','email','password')


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('mobile_no',)
