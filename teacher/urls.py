
from django.urls import path

from . import views

urlpatterns = [
    path('teacher-home/', views.teacher_home, name='teacher_home'),
    path('teacher-registration/', views.teacher_registration, name='teacher_registration'),
    path('teacher-login/', views.teacher_login_page, name='teacher_login'),
    path("forgot-password/teacher/", views.forgot_password, name='forgot_password_teacher'),
    path('try-page/', views.try_page, name='try'),
]
