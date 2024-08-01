from django.db import models
from django.db import models
from django.core.exceptions import ValidationError


def validate_password_length(value):
    if len(value) != 8:
        raise ValidationError("Password must be 8 characters long.")


class StaffLogin(models.Model):
    user_id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=8, null=False, blank=False, validators=[validate_password_length])

    def __str__(self):
        return f"{self.user_id} - {self.password}"
    
    
class Departments(models.Model):
    department_id = models.IntegerField(primary_key=True)
    department_name = models.CharField(max_length=100)
    def __str__(self):
        return self.department_name

class Courses(models.Model):
    course_id = models.IntegerField(primary_key=True)
    course_name = models.CharField(max_length=100)
    total_credit = models.IntegerField()
    duration = models.IntegerField()
    department = models.ForeignKey(Departments, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.course_name)
class Student(models.Model):
    student_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    user_id = models.IntegerField(unique=True)
    password = models.CharField(max_length=8, null=False, blank=False,validators=[validate_password_length])
    department = models.ForeignKey(Departments, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student_id} - {self.name}"

    class Meta:
        verbose_name_plural = 'Students' 


class Creditss(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    credit_acquired = models.IntegerField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('course', 'student')

class CompletedCourses(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    

class Staff(models.Model):
    staff_id = models.IntegerField(primary_key=True)
    staff_name = models.CharField(max_length=100, null=False)
    user = models.ForeignKey(StaffLogin, on_delete=models.CASCADE)




# Create your models here.


# Create your models here.
