import datetime
from email.policy import default

from sqlalchemy import ForeignKey
from sqlalchemy.orm import backref

from .import db
from flask_login import UserMixin


class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name= db.Column(db.String(100))
    workouts = db.relationship('Workout',backref = 'author',lazy = True)

class Workout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pushups = db.Column(db.Integer, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.UTC)
    comment = db.Column(db.Text, nullable = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable = False)