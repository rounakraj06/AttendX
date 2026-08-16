# AttendX — Smart Attendance Management System

> A full-stack attendance management platform built to simplify academic attendance, student management, and teacher workflows with a focus on automation and face-recognition-based attendance.
>
> ## 🌐 Live Demo

- **Student Portal:** [Open Student Portal](https://attendx-1-ytgn.onrender.com)
- **Teacher Portal:** [Open Teacher Portal](https://attendx-1-ytgn.onrender.com/teacher_login/)

## 🚀 About AttendX

AttendX is a web-based academic management project designed to make everyday attendance management more organized, accessible, and efficient.

The system provides separate experiences for students and teachers, combining attendance management, academic records, study resources, and administrative features in one platform.

This project was designed and developed as a real-world BCA project with a focus on practical problem solving, responsive UI, backend development, database management, and computer-vision integration.

## ✨ Key Features

### 🤖 Face Recognition Attendance
- Face-based student identification for attendance
- Camera-based attendance workflow
- Face recognition module integrated with the Django backend
- Attendance session management
- Attendance records stored in the database

### 👨‍🎓 Student Portal
- Student authentication
- Personal profile
- Attendance overview
- Academic marks
- Study notes and resources
- Library access
- Attendance status

### 👨‍🏫 Teacher Portal
- Teacher authentication
- Student management
- Start and manage attendance sessions
- Manual attendance management
- Attendance reports
- Internal marks management
- Library/resource management
- Teacher settings and password management

### 📊 Academic Management
- Attendance records
- Internal marks
- Student information
- Attendance reports
- Semester-wise academic resources
- Notes and previous-year papers

### 📚 Learning Resources
- Digital notes
- Previous-year papers
- Library resources
- Semester-wise study material
- Academic PDFs

### 🔐 Authentication & Profiles
- Student and teacher login systems
- Profile management
- Password management
- Role-based dashboard experience
  
## 📸 Project Screenshots

### 🏠 Home & Student Experience

<p align="center">
  <img src="screenshots/home.png" width="48%" />
</p>

### 👨‍🎓 Student Dashboard

<p align="center">
  <img src="screenshots/student-dashboard.png" width="48%" />
  <img src="screenshots/attendance.png" width="48%" />
</p>

### 🤖 Face Recognition Attendance

<p align="center">
  <img src="screenshots/face-attendance.png" width="48%" />
  <img src="screenshots/face-attendance-session.png" width="48%" />
</p>

### 👨‍🏫 Teacher Portal

<p align="center">
  <img src="screenshots/teacher-login.png" width="48%" />
  <img src="screenshots/teacher-dashboard.png" width="48%" />
</p>

### 📚 Academic Resources

<p align="center">
  <img src="screenshots/library.png" width="48%" />
  <img src="screenshots/marks.png" width="48%" />
</p>

## 🛠️ Technology Stack

### Backend
- Python
- Django
- SQLite

### Computer Vision
- OpenCV
- face-recognition
- dlib

### Frontend
- HTML5
- CSS3
- JavaScript

### Storage & Deployment
- Cloudinary integration
- Docker configuration
- Git & GitHub

## 🏗️ Project Structure

## 🔄 How AttendX Works

AttendX connects students, teachers, attendance sessions, academic records, and learning resources into a single web-based platform.

```text
                    ┌─────────────────────┐
                    │       AttendX       │
                    │   Web Application   │
                    └──────────┬──────────┘
                               │
              ┌────────────────┴────────────────┐
              │                                 │
      ┌───────▼────────┐               ┌────────▼────────┐
      │ Student Portal │               │ Teacher Portal  │
      └───────┬────────┘               └────────┬────────┘
              │                                 │
       ┌──────▼───────┐                  ┌──────▼─────────┐
       │   Student    │                  │    Manage      │
       │ Authentication│                  │    Students    │
       └──────┬───────┘                  └──────┬─────────┘
              │                                 │
       ┌──────▼────────────┐             ┌──────▼─────────┐
       │ Attendance &      │             │ Attendance     │
       │ Academic Records  │             │ Sessions       │
       └──────┬────────────┘             └──────┬─────────┘
              │                                 │
              │                         ┌───────▼─────────┐
              │                         │ Face Recognition│
              │                         │    Workflow     │
              │                         └───────┬─────────┘
              │                                 │
              └────────────────┬────────────────┘
                               │
                      ┌────────▼────────┐
                      │ Django Backend  │
                      │ + Database      │
                      └────────┬────────┘
                               │
                    ┌──────────▼──────────┐
                    │ Attendance Records │
                    │ Marks & Resources  │
                    └─────────────────────┘

```text
AttendX/
├── accounts/              # Application logic, models and views
├── config/                # Django project configuration
├── templates/             # HTML templates
├── static/                # CSS, JavaScript and static assets
├── profile_photos/        # Profile-related resources
├── media/                 # Uploaded media
├── manage.py              # Django management entry point
├── requirements.txt       # Python dependencies
└── Dockerfile             # Container configuration
