
from django.shortcuts import render, redirect

from django.contrib.auth import get_user_model, login, authenticate

from .forms import Student_Registration, Student_Login

from .models import StudentRegistration

# Student home function display main things link login display and assignment display.
def student_home(request):
	return render(request, 'student/student_home.html')

# Login function so that student can login and complete the assignment.
def student_login(request):
	student_login_form = Student_Login(request.POST or None)
	if request.POST:
		username = request.POST.get("username")
		password = request.POST.get("password")
		user = authenticate(username=username, password=password)
		login(request, user)
		return redirect("/")
	return render(request, 'login/student_login.html', {'student_login_form':student_login_form})

# Register function so that if a student has not register him self or her self he can register.
User = get_user_model()
def student_register(request):
	student_form = Student_Registration(request.POST or None)
	#  if the form is valid(see- student/forms.py) save the data into Database(see- student/models.py) for further work
	if student_form.is_valid():
		username = request.POST.get("username")
		first_name = request.POST.get("first_name")
		last_name = request.POST.get("last_name")
		student_class =  request.POST.get("student_class")
		student_email =  request.POST.get("student_email")
		student_id = request.POST.get("student_id")
		phone_number = request.POST.get("phone_number")
		student_password = request.POST.get("student_password")
		x = StudentRegistration.objects.create(username=username, first_name=first_name, last_name=last_name, student_class=student_class, student_id=student_id, student_email=student_email, phone_number=phone_number, student_password=student_password)
		if x:
			new_user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, password=student_password, email=student_email)
			login(request, new_user)
		return redirect("/")
	return render(request, 'registration/student_registration.html', {'student_form':student_form})
