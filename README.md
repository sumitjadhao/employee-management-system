# 👥 Employee Management System (EMS)

A full-stack web application built with **Django** to manage employees, track attendance with **webcam selfie verification**, calculate payroll automatically, and handle leave requests through an approval workflow. The app has separate dashboards for **Admin** and **Employee** roles and is deployed live on **Railway**.

> 🔗 **Live Demo:** `ADD-YOUR-RAILWAY-URL-HERE`
> 📂 **Repository:** [github.com/sumitjadhao/employee-management-system](https://github.com/sumitjadhao/employee-management-system)

---

## 📌 Table of Contents

- [About the Project](#-about-the-project)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Getting Started](#-getting-started)
- [Environment Variables](#-environment-variables)
- [Deployment](#-deployment)
- [Usage](#-usage)
- [Future Improvements](#-future-improvements)
- [Author](#-author)

---

## 📖 About the Project

Small and mid-sized organisations often manage attendance, salary and leave with paper registers or scattered spreadsheets, which is slow and error-prone. This project brings everything into one web portal:

- Admins manage employees, review attendance, approve leave and see payroll in one place.
- Employees check in/out, apply for leave and view their own records and dashboard.

The goal of this project was to build a complete, production-style Django application — from database design and authentication to deployment on a live server.

---

## ✨ Features

### 🔐 Authentication & Roles
- Secure login system with **role-based access control** (Admin / Employee)
- Each role sees only the pages and actions meant for them

### 👤 Employee Management (Admin)
- Add, view, update and delete employee records (**CRUD**)
- Centralised employee database

### 📸 Webcam Selfie Attendance
- Employees **check in and check out** using a selfie captured from the webcam
- Attendance is recorded against the logged-in employee
- Helps verify that the employee is actually present

### 💰 Automatic Payroll Calculation
- Salary is **calculated automatically** from the employee's attendance records
- No manual calculation needed by the admin

### 🌴 Leave Management
- Employees submit **leave requests**
- Admin **approves or rejects** requests through an approval workflow
- Employees can track the status of their requests

### 📊 Dashboards
- **Admin Dashboard:** overview of employees, attendance, leave requests and payroll
- **Employee Dashboard:** personal attendance, leave status and related details

---

## 🛠 Tech Stack

| Layer | Technology |
|---|---|
| **Backend** | Python, Django |
| **Database** | MySQL |
| **Frontend** | HTML, CSS, Vanilla JavaScript |
| **Production Server** | Gunicorn |
| **Static Files** | WhiteNoise |
| **Config Management** | python-decouple |
| **Version Control** | Git & GitHub |
| **Deployment** | Railway |

---

## 🚀 Getting Started

Follow these steps to run the project on your local machine.

### Prerequisites

- Python 3.8 or higher
- MySQL Server
- Git
- A webcam (needed for the selfie attendance feature)

### 1. Clone the repository

```bash
git clone https://github.com/sumitjadhao/employee-management-system.git
cd employee-management-system
```

### 2. Create and activate a virtual environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux / macOS
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create the MySQL database

```sql
CREATE DATABASE ems_db;
```

### 5. Configure environment variables

Create a `.env` file in the project root (same folder as `manage.py`) and add your values. See [Environment Variables](#-environment-variables) below.

### 6. Run migrations

```bash
python manage.py migrate
```

### 7. Create an admin (superuser) account

```bash
python manage.py createsuperuser
```

### 8. Start the development server

```bash
python manage.py runserver
```

Open **http://127.0.0.1:8000/** in your browser.

---

## 🔑 Environment Variables

The project uses **python-decouple** to keep secrets out of the source code. Create a `.env` file like this:

```env
SECRET_KEY=your-django-secret-key
DEBUG=True

DB_NAME=ems_db
DB_USER=your-mysql-username
DB_PASSWORD=your-mysql-password
DB_HOST=localhost
DB_PORT=3306
```

> ⚠️ Never commit your `.env` file to GitHub. Make sure `.env` is listed in `.gitignore`.
>
> The variable names above are examples — keep them the same as the ones used in your `settings.py`.

---

## ☁️ Deployment

The application is deployed on **Railway**.

- **Gunicorn** runs the Django app in production
- **WhiteNoise** serves static files
- Environment variables (secret key, database credentials, etc.) are configured in the Railway dashboard instead of a `.env` file
- Run `python manage.py collectstatic` to gather static files before/during deployment

---

## 📘 Usage

**As Admin**
1. Log in with the admin credentials
2. Add employees from the employee management section
3. Monitor attendance and payroll from the dashboard
4. Approve or reject leave requests

**As Employee**
1. Log in with the credentials given by the admin
2. Allow camera access and mark **check-in** / **check-out** with a selfie
3. Apply for leave and track its status
4. View your personal dashboard

---

## 🔮 Future Improvements

- Email notifications for leave approval/rejection
- Export payroll and attendance reports (PDF / Excel)
- Face recognition to automatically verify selfie attendance
- Department-wise and monthly analytics charts
- REST API for a mobile app

---

## 👨‍💻 Author

**Sumit Raju Jadhao**
B.Sc. IT, Mumbai University (2026)

- GitHub: [@sumitjadhao](https://github.com/sumitjadhao)
- Email: sumitjadhao.info@gmail.com

---

⭐ If you found this project useful, consider giving it a star on GitHub!
