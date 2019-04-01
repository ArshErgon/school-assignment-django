from django.db import models

class TeacherRegistration(models.Model):
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(default=True)
    class_teacher_of = models.CharField(max_length=5)
    password = models.CharField(max_length=100)

    def __str__(self):
        return ("%s class teacher of %s" % (self.first_name + ' ' + self.last_name, str(self.class_teacher_of)))


class TryModel(models.Model):
    photo = models.ImageField(upload_to='try')
