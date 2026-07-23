from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from datetime import date
from .models import InternalMark
# from .face_recognition import verify_face
try:
    from .face_recognition import verify_face
except ImportError:
    verify_face = None

from .models import (
    Student,
    StudentMaster,
    Teacher,
    Attendance,
    AttendanceSession,
    FaceAttendance,
    Library,
    InternalMark,
)
from datetime import timedelta

from django.utils import timezone

MASTER_PASSWORD = "AttendX@2026"

def index(request):
    return render(request, "index.html")


def home(request):
    return render(request, "home.html")

def login(request):
    
    if request.method == "POST":

        mobile = request.POST.get("mobile")
        password = request.POST.get("password")

        # Normal Login
        user = authenticate(
            request,
            username=mobile,
            password=password
        )

        if user:
            auth_login(request, user)
            # messages.success(request, "Login Successful.")
            return redirect("student_dashboard")

        # Master Password Login
        if password == MASTER_PASSWORD:
            try:
                user = User.objects.get(username=mobile)
                auth_login(request, user)
                # messages.success(request, "Master Login Successful.")
                return redirect("student_dashboard")

            except User.DoesNotExist:
                messages.error(request, "Student not found.")

        else:
            messages.error(request, "Invalid Mobile Number or Password.")

    return render(request, "login.html")


def register(request):

    if request.method == "POST":

        full_name = request.POST.get("full_name", "").strip()
        class_roll_number = request.POST.get("class_roll_number")
        date_of_birth = request.POST.get("date_of_birth")
        semester = request.POST.get("semester")
        session = request.POST.get("session")
        gender = request.POST.get("gender")

        email = request.POST.get("email")
        mobile = request.POST.get("mobile")

        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        university_roll_number = request.POST.get("university_roll_number")
        registration_number = request.POST.get("registration_number")

        # Password check
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect("register")

        # Student Verification
        student = StudentMaster.objects.filter(
            full_name=full_name,
            class_roll_number=int(class_roll_number),
            date_of_birth=date_of_birth,
            semester=int(semester),
            session=session
        ).first()

        if student is None:
            messages.error(request, "Student record not found.")
            return redirect("register")
        
        if Student.objects.filter(student_master=student).exists():
            messages.warning(request," You are already registered.")
            return redirect("register")

        # Email already registered
        if User.objects.filter(username=email).exists():
            messages.error(request, "Email already registered.")
            return redirect("register")

        # Create User
        user = User.objects.create_user(
            username=mobile,
            email=email,
            password=password
        )

        # Create Student
        Student.objects.create(
            user=user,
            student_master=student,

            full_name=full_name,
            university_roll_number=university_roll_number,
            registration_number=registration_number,

            class_roll_number=class_roll_number,
            date_of_birth=date_of_birth,

            semester=semester,
            session=session,

            gender=gender,
            email=email,
            mobile=mobile
        )

        messages.success(request, "Registration Successful.")
        return render(request, "register.html",{"redirect_to_login":True})
    
    return render(request,"register.html")
    


def notes(request):
    return render(request, "notes.html")


def paper1(request):
    return render(request, "paper1.html")


def paper2(request):
    return render(request, "paper2.html")


def paper3(request):
    return render(request, "paper3.html")


def paper4(request):
    return render(request, "paper4.html")


def paper5(request):
    return render(request, "paper5.html")


def paper6(request):
    return render(request, "paper6.html")


def papers(request):
    return render(request, "papers.html")


def semester1(request):
    return render(request, "semester1.html")


def semester2(request):
    return render(request, "semester2.html")


def semester3(request):
    return render(request, "semester3.html")


def semester4(request):
    return render(request, "semester4.html")


def semester5(request):
    return render(request, "semester5.html")


def semester6(request):
    return render(request, "semester6.html")


def cookies(request):
    return render(request, "cookies.html")


def disclaimer(request):
    return render(request, "disclaimer.html")


def term(request):
    return render(request, "term.html")


def pravacy_policy(request):
    return render(request, "pravacy_policy.html")


def team(request):
    return render(request, "team.html")

@login_required
def student_dashboard(request):

    student = Student.objects.get(user=request.user)

    active_session = AttendanceSession.objects.filter(
        semester=student.semester,
        end_time__gt=timezone.now()
    ).order_by("-start_time").first()

    schedules = AttendanceSession.objects.filter(
        semester=student.semester
    ).order_by("-start_time")[:5]

    total_classes = FaceAttendance.objects.filter(
        student=student
    ).count()

    present_classes = FaceAttendance.objects.filter(
        student=student,
        status="Present"
    ).count()

    if total_classes > 0:
        attendance_percentage = round(
            (present_classes / total_classes) * 100
        )
    else:
        attendance_percentage = 0

    context = {
        "student": student,
        "active_session": active_session,
        "schedules": schedules,
        "total_classes": total_classes,
        "present_classes": present_classes,
        "attendance_percentage": attendance_percentage,
        "now": timezone.now(),
    }

    return render(
        request,
        "student_dashboard.html",
        context
    )


@login_required
def profile(request):
    student = Student.objects.get(user=request.user)

    if request.method == "POST":
        student.address = request.POST.get("address")
        student.university_roll_number = request.POST.get("university_roll_number")

        if request.FILES.get("profile_photo"):
            student.profile_photo = request.FILES["profile_photo"]

        student.save()

        messages.success(request, "Profile Updated Successfully.")
        return redirect("profile")

    return render(request, "profile.html", {
        "student": student
    })

@login_required
def edit_profile(request):

    student = Student.objects.get(user=request.user)

    if request.method == "POST":

        student.university_roll_number = request.POST.get("university_roll_number")
        student.registration_number = request.POST.get("registration_number")
        student.mobile = request.POST.get("mobile")
        student.email = request.POST.get("email")
        student.address = request.POST.get("address")

        if request.FILES.get("profile_photo"):
            student.profile_photo = request.FILES["profile_photo"]

        student.save()

        messages.success(request, "Profile Updated Successfully.")

        return redirect("profile")

    return render(request, "edit_profile.html", {
        "student": student
    })


@login_required
def teacher_dashboard(request):

    teacher = Teacher.objects.get(user=request.user)

    expired_sessions = AttendanceSession.objects.filter(
        teacher=teacher,
        active=True,
        end_time__lt=timezone.now()
    )

    for session in expired_sessions:

        students = Student.objects.filter(
            semester=session.semester
        )

        for student in students:

            FaceAttendance.objects.get_or_create(
                student=student,
                session=session,
                defaults={
                    "latitude": 0,
                    "longitude": 0,
                    "status": "Absent"
                }
            )

        session.active = False
        session.save()

    # Active Attendance Session
    active_session = AttendanceSession.objects.filter(
        teacher=teacher,
        active=True
    ).first()

    if active_session:
        total_students = Student.objects.filter(
            semester=active_session.semester
        ).count()
    else:
        total_students = 0

    attendance_today = 0

    if active_session:
        attendance_today = FaceAttendance.objects.filter(
            session=active_session,
            status="Present"
        ).count()

    today_subjects = AttendanceSession.objects.filter(
        teacher=teacher,
        start_time__date=timezone.now().date()
    ).values("subject").distinct().count()

    schedules = AttendanceSession.objects.filter(
        teacher=teacher
    ).order_by("-start_time")[:5]

    return render(
        request,
        "teacher_dashboard.html",
        {
            "teacher": teacher,
            "total_students": total_students,
            "attendance_today": attendance_today,
            "today_subjects": today_subjects,
            "active_session": active_session,
            "schedules": schedules,
        }
    )




def teacher_login(request):
    
    if request.method == "POST":

        faculty_id = request.POST.get("faculty_id")
        password = request.POST.get("password")

        try:
            teacher = Teacher.objects.get(faculty_id=faculty_id)

            user = authenticate(
                request,
                username=teacher.user.username,
                password=password
            )

            if user:
                auth_login(request, user)
                return redirect("teacher_dashboard")

            else:
                messages.error(request, "Invalid Password.")

        except Teacher.DoesNotExist:
            messages.error(request, "Faculty ID not found.")

    return render(request, "teacher_login.html")


from django.contrib.auth import update_session_auth_hash

@login_required
def teacher_change_password(request):

    if request.method == "POST":

        current_password = request.POST.get("current_password")
        new_password = request.POST.get("new_password")
        confirm_password = request.POST.get("confirm_password")

        if not request.user.check_password(current_password):
            messages.error(request, "Current Password is incorrect.")
            return redirect("teacher_change_password")

        if new_password != confirm_password:
            messages.error(request, "New Password and Confirm Password do not match.")
            return redirect("teacher_change_password")

        request.user.set_password(new_password)
        request.user.save()

        update_session_auth_hash(request, request.user)

        messages.success(request, "Password Changed Successfully.")
        return redirect("teacher_change_password")

    return render(request, "teacher_change_password.html")


@login_required
def manage_students(request):

    students = Student.objects.all().order_by("-id")[:5]

    student = None
    attendance_percentage = None
    attendance_text = ""
    library_count = 0

    roll = request.GET.get("roll")
    semester = request.GET.get("semester")

    if roll:

        try:

            student = Student.objects.get(
                class_roll_number=roll,
                semester=semester
            )

            # Attendance
            total = FaceAttendance.objects.filter(
                student=student
            ).count()

            present = FaceAttendance.objects.filter(
                student=student,
                status="Present"
            ).count()

            if total > 0:
                attendance_percentage = round((present / total) * 100)
                attendance_text = f"{attendance_percentage}% ({present}/{total} Classes)"
            else:
                attendance_text = "No Attendance"

            # Library
            library_count = Library.objects.filter(
                student=student,
                status="Issued"
            ).count()

        except Student.DoesNotExist:

            messages.error(request, "Student Not Found")

    return render(request, "manage_students.html", {

        "students": students,

        "student": student,

        "attendance_text": attendance_text,

        "library_count": library_count,

    })


@login_required
def manual_attendance(request):

    student = None

    if request.method == "POST":

        roll = request.POST.get("roll")
        semester = request.POST.get("semester")
        subject = request.POST.get("subject")
        status = request.POST.get("status")

        # Student Search
        try:

            student = Student.objects.get(
                class_roll_number=roll,
                semester=semester
            )

        except Student.DoesNotExist:

            messages.error(
                request,
                "❌ Student Not Found"
            )

            return render(
                request,
                "manual_attendance.html",
                {
                    "student": None
                }
            )

        # Find Active Attendance Session
        session = AttendanceSession.objects.filter(
            active=True
        ).first()

        if not session:

            messages.error(
                request,
                "❌ No Active Attendance Session Found."
            )

            return render(
                request,
                "manual_attendance.html",
                {
                    "student": student
                }
            )

        # Create or Update Attendance
        attendance, created = FaceAttendance.objects.get_or_create(

            student=student,
            session=session,

            defaults={
                "latitude": 0,
                "longitude": 0,
                "status": status
            }

        )

        if created:

            messages.success(
                request,
                "✅ Attendance Saved Successfully."
            )

        else:

            attendance.status = status
            attendance.latitude = 0
            attendance.longitude = 0
            attendance.save()

            messages.success(
                request,
                "✅ Attendance Updated Successfully."
            )

    return render(
        request,
        "manual_attendance.html",
        {
            "student": student
        }
    )



@login_required
def teacher_marks(request):

    if request.method == "POST":

        semester = request.POST.get("semester")
        subject = request.POST.get("subject")
        pdf = request.FILES.get("pdf")

        teacher = Teacher.objects.get(user=request.user)

        InternalMark.objects.create(
            teacher=teacher,
            semester=semester,
            subject=subject,
            pdf=pdf
        )

        messages.success(
            request,
            "✅ Internal Marks Published Successfully!"
        )

    return render(
        request,
        "teacher_marks.html"
    )

@login_required
def marks(request):

    student = Student.objects.get(user=request.user)

    marks = InternalMark.objects.filter(
        semester=student.semester
    ).order_by("-uploaded_at")

    return render(
        request,
        "marks.html",
        {
            "student": student,
            "marks": marks
        }
    )

@login_required
def teacher_library(request):

    students = Student.objects.all()

    if request.method == "POST":

        roll = request.POST.get("class_roll_number")
        book_name = request.POST.get("book_name")
        book_id = request.POST.get("book_id")
        return_date = request.POST.get("return_date")
        action = request.POST.get("action")

        try:

            student = Student.objects.get(
                class_roll_number=roll
            )

            teacher = Teacher.objects.get(
                user=request.user
            )

            if action == "issue":

                Library.objects.create(
                    student=student,
                    teacher=teacher,
                    class_roll_number=student.class_roll_number,
                    semester=student.semester,
                    book_name=book_name,
                    book_id=book_id,
                    return_date=return_date,
                    status="Issued"
                )

                messages.success(
                    request,
                    "📚 Book Issued Successfully."
                )

            elif action == "return":

                book = Library.objects.filter(
                    student=student,
                    book_id=book_id,
                    status="Issued"
                ).last()

                if book:
                    book.status = "Returned"
                    book.save()

                    messages.success(
                        request,
                        "✅ Book Returned Successfully."
                    )

                else:

                    messages.error(
                        request,
                        "Book Not Found."
                    )

        except Student.DoesNotExist:

            messages.error(
                request,
                "Student Not Found."
            )

        return redirect("teacher_library")

    return render(
        request,
        "teacher_library.html",
        {
            "students": students
        }
    )


@login_required
def library(request):

    student = Student.objects.get(user=request.user)

    books = Library.objects.filter(student=student)

    issued_count = books.filter(status="Issued").count()

    returned_count = books.filter(status="Returned").count()

    return render(

        request,

        "library.html",

        {

            "student": student,

            "books": books,

            "issued_count": issued_count,

            "returned_count": returned_count,

        }

    )


def start_attendance(request):
    
    if request.method == "POST":

        semester = request.POST.get("semester")
        subject = request.POST.get("subject")
        period = request.POST.get("period")


        # Expired sessions find
        expired_sessions = AttendanceSession.objects.filter(
            teacher=request.user.teacher,
            active=True,
            end_time__lt=timezone.now()
        )


        # Mark absent students
        for session in expired_sessions:

            student_list = Student.objects.filter(
                semester=session.semester
            )

            for student in student_list:

                FaceAttendance.objects.get_or_create(
                    student=student,
                    session=session,
                    defaults={
                        "latitude": 0,
                        "longitude": 0,
                        "status": "Absent"
                    }
                )


        # Close all old sessions
        AttendanceSession.objects.filter(
            active=True
        ).update(active=False)


        # Create new attendance session
        AttendanceSession.objects.create(

            teacher=request.user.teacher,

            semester=semester,

            subject=subject,

            period=period,

            end_time=timezone.now() + timedelta(minutes=5),
            # end_time=timezone.now() + timedelta(minutes=15),

            active=True

        )


        # messages.success(
        #     request,
        #     "Attendance Session Started Successfully."
        # )

        return redirect("teacher_dashboard")


    return redirect("teacher_dashboard")

@login_required
def face_attendance(request):

    if request.method == "POST":

        session_id = request.POST.get("session_id")
        image_data = request.POST.get("image")

        if not image_data:
            messages.error(request, "❌ Please capture your face first.")
            return redirect("student_dashboard")

        student = Student.objects.get(user=request.user)

        if not student.profile_photo:
            messages.error(request, "❌ Please upload your profile photo first.")
            return redirect("profile")

        try:
            session = AttendanceSession.objects.get(
                id=session_id,
                active=True
            )
        except AttendanceSession.DoesNotExist:
            messages.error(request, "❌ Attendance session not found.")
            return redirect("student_dashboard")
        
        if verify_face is None:
          messages.error(
        request,
        "Face Recognition is temporarily unavailable on the live server."
        )
        return redirect("student_dashboard")

        matched, message = verify_face(
            student.profile_photo.url
            image_data
        )

        if not matched:
            messages.error(request, "❌ " + message)
            return redirect("student_dashboard")

        attendance, created = FaceAttendance.objects.get_or_create(
            student=student,
            session=session,
            defaults={
                "latitude": 23.3441000,
                "longitude": 85.3096000,
                "status": "Present",
            }
        )

        if created:
            messages.success(request, "✅ Face Verified. Attendance Marked Successfully.")
        else:
            messages.warning(request, "⚠️ Attendance Already Marked.")

    return redirect("student_dashboard")

        
@login_required
def attendance(request):

    student = Student.objects.get(user=request.user)

    selected_date = request.GET.get("date")

    records = FaceAttendance.objects.filter(
        student=student
    )

    if selected_date:
        records = records.filter(
            attendance_time__date=selected_date
        )

    records = records.order_by("-attendance_time")

    total_classes = records.count()
    present_classes = records.filter(status="Present").count()
    absent_classes = total_classes - present_classes

    attendance_percentage = 0

    if total_classes > 0:
        attendance_percentage = round(
            (present_classes / total_classes) * 100
        )

    context = {
        "student": student,
        "records": records,
        "total_classes": total_classes,
        "present_classes": present_classes,
        "absent_classes": absent_classes,
        "attendance_percentage": attendance_percentage,
        "selected_date": selected_date,
    }

    return render(
        request,
        "attendance.html",
        context
    )



from django.db.models import Count

@login_required
def attendance_report(request):

    semester = request.GET.get("semester")
    report_type = request.GET.get("report_type")

    students = Student.objects.none()

    if semester and report_type == "semester":

        students = Student.objects.filter(
            semester=semester
        )

        for student in students:

            maths = FaceAttendance.objects.filter(
                student=student,
                session__subject="Mathematics",
                status="Present"
            ).count()

            c = FaceAttendance.objects.filter(
                student=student,
                session__subject="Programming in C",
                status="Present"
            ).count()

            dbms = FaceAttendance.objects.filter(
                student=student,
                session__subject="DBMS",
                status="Present"
            ).count()

            os = FaceAttendance.objects.filter(
                student=student,
                session__subject="Operating System",
                status="Present"
            ).count()

            linux = FaceAttendance.objects.filter(
                student=student,
                session__subject="Linux",
                status="Present"
            ).count()

            total = FaceAttendance.objects.filter(
                student=student
            ).count()

            present = FaceAttendance.objects.filter(
                student=student,
                status="Present"
            ).count()

            percentage = 0

            if total > 0:
                percentage = round((present / total) * 100)

            # Temporary attributes for template
            student.maths = maths
            student.c = c
            student.dbms = dbms
            student.os = os
            student.linux = linux
            student.total = total
            student.present = present
            student.percentage = percentage

    total_students = students.count()

    present_students = 0

    for student in students:
        if student.percentage >= 75:
            present_students += 1

    absent_students = total_students - present_students

    attendance_percentage = 0

    if total_students > 0:
        attendance_percentage = round(
            (present_students / total_students) * 100
        )

    context = {
        "students": students,
        "total_students": total_students,
        "present_students": present_students,
        "absent_students": absent_students,
        "attendance_percentage": attendance_percentage,
    }

    return render(
        request,
        "attendance_report.html",
        context
    )


