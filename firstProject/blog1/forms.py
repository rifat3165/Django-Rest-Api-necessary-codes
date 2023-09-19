from typing import Any
from django import forms
from django.core import validators

class TeacherRegistration(forms.Form):
    first_name = forms.CharField(label='Enter your First Name', label_suffix=" ", initial="Rifat")
    last_name = forms.CharField(label='Enter your Last Name', label_suffix=" ", initial='Monjurul')
    email = forms.EmailField(initial='rifat@gmail.com', label_suffix=" ", disabled=True)
    password = forms.CharField(label="Enter Password", label_suffix=" ", widget=forms.PasswordInput)
    repassword = forms.CharField(label="Enter Re-password", label_suffix=" ", widget=forms.PasswordInput)
    textarea = forms.CharField(label='Write here', label_suffix=" ", widget=forms.Textarea)
    file = forms.CharField(widget=forms.FileInput)
    checkbox = forms.CharField(widget=forms.CheckboxInput)


    def clean(self):
        cleaned_data = super().clean()
        rightpass = self.cleaned_data['password']
        worngpass = self.cleaned_data['repassword']

        if rightpass != worngpass:
            raise forms.ValidationError("Password doesn't match")