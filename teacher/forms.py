from django import forms

from .models import TryModel

from django.contrib.auth import get_user_model

#  Why I am not using models form because models can not be style
User = get_user_model()
class Teacher_Registration(forms.Form):
    CHOICES = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
        ('0', 'none'),
    ]
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    class_teacher_of = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}), choices=CHOICES)
    phone_number = forms.CharField(max_length="10", widget=forms.NumberInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder': 'length of 3'}))
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={'class':'form-control'}))

# check for username if it is smae give error

    def clean_username(self):
        username = self.cleaned_data.get("username")
        check_name = User.objects.filter(username=username)
        if check_name.exists():
            raise forms.ValidationError("Username is taken think another one")
        return username


    def clean(self):
        data = self.cleaned_data.get
        password1 = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password2 != password1:
            raise forms.ValidationError("Password does not match")
        if len(password1) < 3:
            raise forms.ValidationError("Password must have 3 letters")
        return data

class Teacher_Login(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":'form-control'}))

class TeacherForgetPassword(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    phone_number = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}))

class TryForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
