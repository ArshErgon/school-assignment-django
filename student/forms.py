from django import forms

from django.contrib.auth import get_user_model

# Student detail also save in data base for further improment or details
User = get_user_model()
class Student_Registration(forms.Form):
    CLASS = [
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
    ]
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    student_class = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    student_id = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'See your I-Card'}))
    student_email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'example@gmail.com'}))
    student_class = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}), choices=CLASS)
    student_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    student_password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))

# check for username if it is smae give error

    def clean_username(self):
        username = self.cleaned_data.get("username")
        check_name = User.objects.filter(username=username)
        if check_name.exists():
            raise forms.ValidationError("Username is taken think another one")
        return username

#  check for password does password1 is password2 or not

    def clean(self):
        data = self.cleaned_data
        password1 = self.cleaned_data.get('student_password')
        password2 = self.cleaned_data.get('student_password2')
        if password2 != password1: # we can use or too or len(password1) != 3 but it will confuse the user
            raise forms.ValidationError("password did't match")
        if len(password1) < 3:
            raise forms.ValidationError("Password must contain 3 letters")
        return data

#  check for studnet id it should be positive not negative

    def clean_student_id(self):
        student_id = self.cleaned_data.get("student_id")
        if int(student_id) <= 0:
            raise forms.ValidationError("Check your id")
        return student_id

class Student_Login(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class":'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
