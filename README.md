Pushups Logger Web App

A simple fitness tracker built with Flask, allowing users to log, update, and delete their pushup workouts. Designed with user authentication and pagination for personal workout logs.

Features
- User authentication with Flask-Login
- Log pushup workouts with optional comments
- Edit or delete existing workouts
- Paginated list of personal workouts
- Route protection for logged-in users only

Tech Stack
- Python 3.7+
- Flask
- Flask-Login
- SQLAlchemy
- WTForms (if used in form handling)
- SQLite (default, can be replaced with any other DB)

Authentication
The /profile, /new, /all, and workout update/delete routes are protected. Users must be logged in to access these routes.

Usage
- Navigate to / — the homepage
- Register/login (depending on your setup)
- Go to /profile to access your account
- Use /new to log a workout
- View all your workouts at /all
- Update or delete workouts from the list
