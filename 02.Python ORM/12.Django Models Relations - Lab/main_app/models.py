from django.db import models
from datetime import date

# 1.The Lecturer


class Lecturer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    lecturer = models.ForeignKey(to=Lecturer,
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 related_name='subjects')

    def __str__(self):
        return f"{self.name}"


# 2.The Student
class Student(models.Model):
    student_id = models.CharField(max_length=10,
                                  primary_key=True)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    email = models.EmailField(unique=True)
    subjects = models.ManyToManyField(to=Subject,
                                      through="StudentEnrollment")


# 3. Enrollment
class StudentEnrollment(models.Model):
    class GradeChoices(models.TextChoices):
        A = ("A", "A")
        B = ("B", "B")
        C = ("C", "C")
        D = ("D", "D")
        F = ("F", "F")

    student = models.ForeignKey(to=Student,
                                on_delete=models.CASCADE)

    subject = models.ForeignKey(to=Subject,
                                on_delete=models.CASCADE)

    enrollment_date = models.DateField(default=date.today)
    grade = models.CharField(max_length=1,
                             choices=GradeChoices.choices,)


# 4 .
class LecturerProfile(models.Model):
    lecturer = models.OneToOneField(to=Lecturer,
                                    on_delete=models.CASCADE,)

    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True,
                           null=True)

    office_location = models.CharField(max_length=100,
                                       blank=True,
                                       null=True)




