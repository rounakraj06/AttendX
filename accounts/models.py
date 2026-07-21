from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class StudentMaster(models.Model):
    full_name = models.CharField(max_length=100)
    class_roll_number = models.PositiveIntegerField()
    date_of_birth = models.DateField()
    semester = models.PositiveSmallIntegerField()
    session = models.CharField(max_length=20)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_master = models.ForeignKey(StudentMaster, on_delete=models.CASCADE)
    

    full_name = models.CharField(max_length=100)
    university_roll_number = models.CharField(max_length=12, blank=True, null=True)
    registration_number = models.CharField(max_length=13, blank=True, null=True)

    class_roll_number = models.PositiveIntegerField()
    date_of_birth = models.DateField()

    semester = models.PositiveSmallIntegerField()
    session = models.CharField(max_length=20)

    gender = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=10)
    address = models.TextField(blank=True, null=True)

    profile_photo = models.ImageField(
    upload_to="profile_photos/",
    blank=True,
    null=True
)


    def __str__(self):
        return self.full_name    


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    faculty_id = models.CharField(max_length=20, unique=True)
    full_name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name
    


class Attendance(models.Model):
    
    STATUS = (
        ("Present", "Present"),
        ("Absent", "Absent"),
        ("Late", "Late"),
    )

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    semester = models.CharField(max_length=20)
    subject = models.CharField(max_length=100)

    date = models.DateField(auto_now_add=True)

    status = models.CharField(
        max_length=10,
        choices=STATUS
    )

    def __str__(self):
        return f"{self.student.full_name} - {self.date}"
    

class InternalMark(models.Model):
    
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE
    )

    semester = models.PositiveSmallIntegerField()

    subject = models.CharField(max_length=100)

    pdf = models.FileField(
        upload_to="internal_marks/"
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"Semester {self.semester} - {self.subject}"
    

class Library(models.Model):
    
    STATUS = (
        ("Issued", "Issued"),
        ("Returned", "Returned"),
    )

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )

    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE
    )

    class_roll_number = models.PositiveIntegerField()

    semester = models.PositiveSmallIntegerField()

    book_name = models.CharField(max_length=200)

    book_id = models.CharField(max_length=50)

    issue_date = models.DateField(auto_now_add=True)

    return_date = models.DateField()

    status = models.CharField(
        max_length=20,
        choices=STATUS,
        default="Issued"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.full_name} - {self.book_name}"



class AttendanceSession(models.Model):
    
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE
    )

    semester = models.PositiveSmallIntegerField()

    subject = models.CharField(max_length=100)

    period = models.CharField(max_length=20)

    start_time = models.DateTimeField(auto_now_add=True)

    end_time = models.DateTimeField()

    active = models.BooleanField(default=True)

    duration = models.PositiveIntegerField(default=5)

    def __str__(self):
        return f"{self.semester} - {self.subject}"
    

    

class FaceAttendance(models.Model):

    STATUS = (
        ("Present", "Present"),
        ("Absent", "Absent"),
    )

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )

    session = models.ForeignKey(
        AttendanceSession,
        on_delete=models.CASCADE
    )

    latitude = models.DecimalField(
        max_digits=10,
        decimal_places=7
    )

    longitude = models.DecimalField(
        max_digits=10,
        decimal_places=7
    )

    attendance_time = models.DateTimeField(auto_now_add=True)

    status = models.CharField(
        max_length=10,
        choices=STATUS,
        default="Present"
    )

    class Meta:
        unique_together = ("student", "session")

    def __str__(self):
        return f"{self.student.full_name} - {self.status}"    
