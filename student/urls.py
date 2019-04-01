
from django.urls import path

from . import views

urlpatterns = [
	path('', views.student_home, name='student_home'),
	path('student-sign-page/', views.student_register, name='student_registration'),
	path("student-login/", views.student_login, name='student_login'),
]
