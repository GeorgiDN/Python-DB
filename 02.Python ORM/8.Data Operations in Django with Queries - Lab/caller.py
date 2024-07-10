import os
import django
from datetime import datetime

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Student
#
# print(Student.objects.all())
# print(type(Student.objects.all()))


# Exam: 01. Add Students
def add_students():
    students = [
        ('FC5204', 'John', 'Doe', '15/05/1995', 'john.doe@university.com'),
        ('FE0054', 'Jane', 'Smith', 'NULL', 'jane.smith@university.com'),
        ('FH2014', 'Alice', 'Johnson', '10/02/1998', 'alice.johnson@university.com'),
        ('FH2015', 'Bob', 'Wilson', '25/11/1996', 'bob.wilson@university.com')
    ]

    for student in students:
        student_id, first_name, last_name, birth_date, email = student

        if birth_date == "NULL":
            student_instance = Student(
                student_id=student_id,
                first_name=first_name,
                last_name=last_name,
                email=email,
            )
            student_instance.save()
        else:
            Student.objects.create(
                student_id=student_id,
                first_name=first_name,
                last_name=last_name,
                birth_date=datetime.strptime(birth_date, '%d/%m/%Y').strftime('%Y-%m-%d'),
                email=email,
            )

# add_students()
# print(Student.objects.all())

# iterate through the records
# for student in Student.objects.all():
#     print(student.__dict__)


# 2 Get Students Info

def get_students_info():
    students_data = []
    for student in Student.objects.all():
        students_data.append(
            f"Student №{student.student_id}:"
            f" {student.first_name}"
            f" {student.last_name};"
            f" Email: {student.email}"
        )

    return '\n'.join(students_data)

# print(get_students_info())


# Exam: 03. Update Students' Emails
def update_students_emails():
    for student in Student.objects.all():
        new_email = student.email.replace('university.com', 'uni-students.com')
        student.email = new_email
        student.save()

# update_students_emails()
# for student in Student.objects.all():
#     print(student.email)


# Exam: 04. Truncate Students
def truncate_students():
    Student.objects.all().delete()


truncate_students()
print(Student.objects.all())
print(f"Number of students: {Student.objects.count()}")
