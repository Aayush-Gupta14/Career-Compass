import os
from flask import Flask, render_template, redirect, url_for
from flask_login import LoginManager, login_required, current_user

from models import db, User
from auth_routes import auth_bp
from dsa_routes import dsa_bp
from internship_routes import internship_bp


app = Flask(__name__, instance_path="/tmp")
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "career-compass-secret")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///career_compass.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


# Initialize Database
db.init_app(app)


# Register Blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(dsa_bp)
app.register_blueprint(internship_bp)


# Flask-Login Setup
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "auth.login"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# Landing Page
@app.route("/")
def index():
    if current_user.is_authenticated:
        return redirect(url_for("home"))

    return redirect(url_for("auth.login"))


# Home Page
@app.route("/home")
@login_required
def home():
    return render_template("home.html")


# Create Database Tables
with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)