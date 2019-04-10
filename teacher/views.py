from django.shortcuts import render, redirect

from .forms import Teacher_Registration, Teacher_Login, TeacherForgetPassword, Add_Assignment, TryForm

from django.contrib.auth import login, get_user_model, authenticate

from .models import TeacherRegistration

from student.models import StudentRegistration

from student.forms import StudentForgotPassword

def teacher_home(request):
    return render(request, 'teacher/teacher_home.html')

# ------------------How its works?--------------
# ==================teacher_registration============
# 1. here we are using a form Teacher_Registration from
# 2. it is taking the username, first_name, password etc fields and create a user for login.
# 3. Then a TeacherRegistration models save all the details why? because once a person misplace or forgot his or her password we can not to recover why? because in user panel password are not save(real password) it save as bashes or hashes.
# 4. Making a TeacherRegistration models we can simply filter by username and display the password.
# 5. Which is what we are doing in forgot_password function.

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
        new_user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password, is_staff=True)
        login(request, new_user)
        TeacherRegistration.objects.create(username=username, first_name=first_name, last_name=last_name, email=email, class_teacher_of=class_teacher_of, phone_number=phone_number ,password=password)
        return redirect("/");

    return render(request, 'registration/teacher_registration.html',{'teacher_form':teacher_form})

# -------------------------How its works?-------------------
# =========================teacher_login_page===============
# 1. it is taking the username and password and the authenticate attribute search for it in the user-panel if it exists login.

def teacher_login_page(request):
    teacher_login_form = Teacher_Login(request.POST or None)
    if request.POST:
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect("/")
    return render(request, 'login/teacher_login.html', {"teacher_login_form":teacher_login_form})

#  ----------------------------------How its works?--------------------------
# ==================================forgot_password==========================
# 1. A forgot_form is the same form for obth student and teacher forgot_form why they are different? teacher forms is different then student form
# 2. A variable person_path store the request path then checks if student or teacher string are present in the path, so that it can display different forms in the smae template
# 3. then the simple condition checks the username, first_name, email in the user-authenticate and if founds search for his/her password from the models.
# 4. Then the forloop to get the attribute password which I can get without using loop.
# 5. And the decide_person, is same.(read 1-4)

def forgot_password(request):
    forgot_form = check_first_name = check_email = check_username = password = ""
    person_path = request.path
    decide_person = ""
    if "student" in person_path:
        decide_person = "student"
    elif "teacher" in person_path:
        decide_person = "teacher"

    print(decide_person)
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
                return render(request, 'login/forgot_password.html', {'forgot_form':forgot_form, 'password':password, 'decide_person':decide_person})
    if "student" in person_path:
        forgot_form = StudentForgotPassword(request.POST or None)
        username = request.POST.get("username")
        email = request.POST.get("email")
        first_name = request.POST.get("first_name")
        phone_number = request.POST.get("phone_number")
        student_id = request.POST.get("student_id")
        check_username = User.objects.filter(username=username)
        check_first_name = User.objects.filter(first_name=first_name)
        check_email = User.objects.filter(email=email)
        if forgot_form.is_valid():
            if check_username.exists() and check_email.exists() and check_first_name.exists():
                passwords = StudentRegistration.objects.filter(student_id=student_id)
                for password in passwords:
                    pass
                password = password.student_password
                return render(request, 'login/forgot_password.html', {'forgot_form':forgot_form, 'password':password , 'decide_person':decide_person})
    return render(request, 'login/forgot_password.html', {'forgot_form':forgot_form, 'decide_person':decide_person})

def teacher_assignment(request):
    form = Add_Assignment(request.POST or None)
    return render(request, "assignment/assignment.html", {'form':form})

def try_page(request):
    form = TryForm(request.POST or None)
    if request.POST:
        username = (request.POST.get("username"))
        password = (request.POST.get('password'))
        user = authenticate(username=username, password=password)
        login(request, user)
    return render(request, 'try.html', {'form':form})
