from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    problems = db.relationship("Problem", backref="user", lazy=True)
    internships = db.relationship("Internship", backref="user", lazy=True)

    def __repr__(self):
        return f"<User {self.username}>"
    


class Problem(db.Model):
    __tablename__ = "problems"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    platform = db.Column(db.String(100), nullable=False)
    difficulty = db.Column(db.String(20), nullable=False)
    topic = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(20), nullable=False)
    notes = db.Column(db.Text)
    user_id = db.Column(
    db.Integer,
    db.ForeignKey("users.id"),
    nullable=False
    )
    def __repr__(self):
        return f"<Problem {self.name}>"


class Internship(db.Model):
    __tablename__ = "internships"

    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    link = db.Column(db.Text)
    application_date = db.Column(db.String(20))
    deadline = db.Column(db.String(20))
    status = db.Column(db.String(30), default="Applied")
    notes = db.Column(db.Text)
    user_id = db.Column(
    db.Integer,
    db.ForeignKey("users.id"),
    nullable=False
    )
    def __repr__(self):
        return f"<Internship {self.company}>"