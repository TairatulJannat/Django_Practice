from django import forms
from django.contrib.auth.models import User
from Login_app.models import UserInfo


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username', 'password' , 'email']

class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo  # Specify the model this form is linked to
        fields = ['facebook_id', 'profile_pic']