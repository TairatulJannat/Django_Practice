from wsgiref.validate import validator

from django import forms
from django.core import validators
from django.forms.widgets import Widget

from first_app import models

class user_form(forms.Form):
    user_name = forms.CharField(label="Full Name", widget=forms.TextInput(attrs={'placeholder':'Enter Full Name','style':'width:300px'}), validators=[validators.MaxLengthValidator(10)])
    user_dob = forms.DateField(label="Date of Birth", widget= forms.TextInput(attrs={'type':'date'}))
    user_email = forms.EmailField(label="Email")
    user_vmail = forms.EmailField(label="Verify Email")
    boolean_field = forms.BooleanField()
    field = forms.CharField(max_length=15, min_length=5)
    choice = forms.ChoiceField(choices=(('','--SELECT OPTION--'),('1','First'),('2','second'),('3','third')))

    def clean(self):
        all_cleaned_data = super().clean()
        user_email = all_cleaned_data.get('user_email')
        user_vmail = all_cleaned_data.get('user_vmail')

        if user_email != user_vmail:
            self.add_error('user_vmail', 'Email fields do not match.')  # Add error to the specific field
            raise forms.ValidationError('Email fields do not match.')  # Raise a general form error

        return all_cleaned_data

class MusicianForm(forms.ModelForm):
    class Meta:
        model = models.Musician
        fields = "__all__"

class AlbumForm(forms.ModelForm):
    release_date = forms.DateField(widget=forms.TextInput(attrs={'type':'date'}))
    class Meta:
        model = models.Album
        fields = "__all__"