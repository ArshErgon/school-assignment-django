
from django.db import models

from datetime import datetime

CLASS_CHOICE = (
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
)


class TeacherRegistration(models.Model):
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(default=True)
    class_teacher_of = models.CharField(max_length=5)
    phone_number = models.IntegerField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return ("%s class teacher of %s" % (self.first_name + ' ' + self.last_name, str(self.class_teacher_of)))

class AddingAssignment(models.Model):
    picture_of_assignment = models.ImageField(upload_to="assignment")
    Class = models.CharField(max_length=2, choices=CLASS_CHOICE, default=1)
    teacher_message = models.TextField()
    adding_time = models.TimeField(auto_now=datetime.now())

    def __str__(self):
        return ("%s added: %s"%(self.Class, str(self.adding_time)))

class TryModel(models.Model):
    photo = models.ImageField(upload_to='try')
