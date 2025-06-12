# 💪 Pushups Logger Web App
Pushups Logger is a lightweight, personal fitness tracker built with Flask. It allows users to securely log, update, and delete their pushup workouts. The app includes user authentication, route protection, and pagination to manage and view workout history efficiently.

## 🔑 Features
- User Authentication (via Flask-Login)
- Log Pushup Workouts with optional comments
- Edit and 🗑️ Delete existing workouts
- Paginated List of personal workout logs
- Protected Routes — accessible only when logged in

## 🛠 Tech Stack
- Component	Technology
- Language	Python 3.7+
- Framework	Flask
- Auth System	Flask-Login
- ORM	SQLAlchemy
- Forms	WTForms (optional)
- Database	SQLite (default)
- Templating	Jinja2

## 🔐 Authentication Details
The following routes are login-protected:
- /profile – View user profile and dashboard
- /new – Log a new workout
- /all – View all personal workouts
- /edit/<id> and /delete/<id> – Modify or remove a workout

Users must be authenticated to access these endpoints.

## 🚀 Usage
- Use the App
- Visit / – Homepage
- Register or log in
- Go to /profile – Access your dashboard
- Log a new workout at /new
- View workout history at /all
- Edit or delete workouts as needed

## ✅ To-Do / Future Enhancements
- Add password hashing (if not implemented yet)
- Graph or stats view of progress over time
- Mobile-friendly UI using Bootstrap
- Workout categories or tags
