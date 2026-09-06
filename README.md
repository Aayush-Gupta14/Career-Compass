# 🧭 Career Compass

Prepare Smarter. Track Better.

Career Compass is a web-based career preparation and tracking application built with **Flask**. It helps students organize their placement preparation by tracking **DSA problems** and **internship applications** in one place.

The application provides user authentication, personalized tracking, progress statistics, and internship status management through a clean and responsive interface.

---

## 🚀 Features

### 🔐 User Authentication

- User registration and login
- Password hashing for secure password storage
- Session-based authentication using Flask-Login
- Logout functionality
- Protected application routes
- Each user can access only their own DSA and internship data

---

### 📚 DSA Tracker

The DSA Tracker helps users maintain a record of coding problems solved during interview preparation.

#### Features

- Add DSA problems
- Store problem name, platform, difficulty, topic, status, and notes
- Track:
  - Total problems
  - Solved problems
  - Easy problems
  - Medium problems
  - Hard problems
- Mark problems as solved
- Delete problems
- Search and filter problems
- User-specific problem tracking

---

### 💼 Internship Tracker

The Internship Tracker helps users organize and monitor internship applications.

#### Features

- Add internship applications
- Store:
  - Company
  - Role
  - Location
  - Application link
  - Application date
  - Deadline
  - Status
  - Notes
- Track application statistics:
  - Total Applications
  - Interviews
  - Offers
  - Rejected
- Progress through application statuses
- Delete applications
- Search and filter applications
- User-specific internship tracking

---

## 🛠️ Tech Stack

### Frontend

- HTML5
- CSS3
- JavaScript
- Jinja2 Templates

### Backend

- Python
- Flask
- Flask Blueprints
- Flask-Login

### Database

- SQLite
- Flask-SQLAlchemy
- SQLAlchemy ORM

### Development

- Git
- GitHub
- VS Code

---

## 🏗️ Project Architecture

Career Compass uses a modular Flask structure with separate route modules for authentication, DSA tracking, and internship tracking.


Career-Compass/
│
├── static/
│   ├── dsastyle.css
│   ├── internship_script.js
│   ├── internshipstyle.css
│   ├── loginstyle.css
│   ├── registerstyle.css
│   ├── script.js
│   └── style.css
│
├── templates/
│   ├── dsa.html
│   ├── home.html
│   ├── internship.html
│   ├── login.html
│   └── register.html
│
├── app.py
├── auth_routes.py
├── dsa_routes.py
├── internship_routes.py
├── models.py
├── requirements.txt
└── .gitignore
