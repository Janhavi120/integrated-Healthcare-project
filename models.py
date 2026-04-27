from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.String(10))
    gender = db.Column(db.String(10))
    symptoms = db.Column(db.String(200))

class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)

class Plan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)