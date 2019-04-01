from django.shortcuts import render, redirect

from .forms import Teacher_Registration, Teacher_Login, TryForm

from django.contrib.auth import login, get_user_model, authenticate

from .models import TeacherRegistration

def teacher_home(request):
    return render(request, 'teacher/teacher_home.html')

User = get_user_model()
def teacher_registration(request):
    teacher_form = Teacher_Registration(request.POST or None)
    if teacher_form.is_valid():
        username = request.POST.get('username')
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        class_teacher_of = request.POST.get("class_teacher_of")
        password = request.POST.get("password")
        new_user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password, is_staff=True)
        login(request, new_user)
        TeacherRegistration.objects.create(username=username, first_name=first_name, last_name=last_name, email=email, class_teacher_of=class_teacher_of, password=password)
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

def try_page(request):
    form = TryForm(request.POST or None)
    if request.POST:
        username = (request.POST.get("username"))
        password = (request.POST.get('password'))
        user = authenticate(username=username, password=password)
        login(request, user)
    return render(request, 'try.html', {'form':form})
