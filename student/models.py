from django.db import models

# 1. Because we use to save the information in the database also why? because student_image
# 2. And if someones password is missing then we can recover it later

class StudentRegistration(models.Model):
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    student_class = models.IntegerField()
    student_id = models.IntegerField()
    student_email = models.EmailField()
    student_password = models.CharField(max_length=100)

    def __str__(self):
        return ("%s of %s class"% (self.first_name + ' ' + self.last_name, str(self.student_class)))
