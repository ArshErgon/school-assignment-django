from django.shortcuts import render, redirect

from .forms import Teacher_Registration, Teacher_Login, TeacherForgetPassword , TryForm

from django.contrib.auth import login, get_user_model, authenticate

from .models import TeacherRegistration

from student.models import StudentRegistration

from student.forms import StudentForgotPassword

def teacher_home(request):
    return render(request, 'teacher/teacher_home.html')

User = get_user_model()
def teacher_registration(request):
    teacher_form = Teacher_Registration(request.POST or None)
    username = request.POST.get('username')
    first_name = request.POST.get("first_name")
    last_name = request.POST.get("last_name")
    email = request.POST.get("email")
    phone_number = request.POST.get("phone_number")
    class_teacher_of = request.POST.get("class_teacher_of")
    password = request.POST.get("password")
    if teacher_form.is_valid():
        print(email)
        new_user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password, is_staff=True)
        login(request, new_user)
        TeacherRegistration.objects.create(username=username, first_name=first_name, last_name=last_name, email=email, class_teacher_of=class_teacher_of, phone_number=phone_number ,password=password)
        return redirect("/");

    return render(request, 'registration/teacher_registration.html',{'teacher_form':teacher_form})

#  we will make a assignment function too where teacher can enter the assignment

def teacher_login_page(request):
    teacher_login_form = Teacher_Login(request.POST or None)
    if request.POST:
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect("/")
    return render(request, 'login/teacher_login.html', {"teacher_login_form":teacher_login_form})

#  forgot-password for student and teacher on the template forget-password
#  ok I have to make it for only teacher only why> because what if student and the teacher share the same name? where it will search for it in teacher_models or student_models
#  it can return the student password

def forgot_password(request):
    forgot_form = check_first_name = check_email = check_username = password = ""
    person_path = request.path
    decide_person = ""
    if "student" in person_path:
        decide_person = "student"

    print(request.path)
    if "teacher" in person_path:
        forgot_form = TeacherForgetPassword(request.POST or None)
        print("here the teacher section start")
        username = request.POST.get("username")
        email = request.POST.get("email")
        first_name = request.POST.get("first_name")
        phone_number = request.POST.get("phone_number")
        check_username = User.objects.filter(username=username)
        check_first_name = User.objects.filter(first_name=first_name)
        check_email = User.objects.filter(email=email)
        print(username)
        if forgot_form.is_valid():
            if check_username.exists() and check_email.exists() and check_first_name.exists():
                passwords = TeacherRegistration.objects.filter(username=username)
                for password in passwords:
                        pass
                password = password.password
                return render(request, 'login/forgot_password.html', {'forgot_form':forgot_form, 'password':password})
    if "student" in person_path:
        forgot_form = StudentForgotPassword(request.POST or None)
        print("we come in the student sections")
        username = request.POST.get("username")
        email = request.POST.get("email")
        first_name = request.POST.get("first_name")
        phone_number = request.POST.get("phone_number")
        student_id = request.POST.get("student_id")
        check_username = User.objects.filter(username=username)
        check_first_name = User.objects.filter(first_name=first_name)
        check_email = User.objects.filter(email=email)
        x = StudentRegistration.objects.filter(student_id=student_id)
        print(x)
        print(StudentRegistration.objects.filter(username=username))
        print(StudentRegistration.objects.filter(first_name=first_name))
        print("working 1")
        if forgot_form.is_valid():
            print("working 2")
            if check_username.exists() and check_email.exists() and check_first_name.exists():
                print("wroking 3")
                passwords = StudentRegistration.objects.filter(student_id=student_id)
                for password in passwords:
                    pass
                password = password.student_password
                return render(request, 'login/forgot_password.html', {'forgot_form':forgot_form, 'password':password})
    return render(request, 'login/forgot_password.html', {'forgot_form':forgot_form, 'decide_person':decide_person})

def try_page(request):
    form = TryForm(request.POST or None)
    if request.POST:
        username = (request.POST.get("username"))
        password = (request.POST.get('password'))
        user = authenticate(username=username, password=password)
        login(request, user)
    return render(request, 'try.html', {'form':form})
