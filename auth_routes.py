from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required,current_user
from models import db, User

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["GET", "POST"])
def register():

    if current_user.is_authenticated:
        return redirect(url_for("home"))

    if request.method == "POST":

       
        username = request.form.get("username", "").strip()
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        
        if not username:
            flash("Username is required.", "error")
            return render_template("register.html")

        if not password:
            flash("Password is required.", "error")
            return render_template("register.html")

        if password != confirm_password:
            flash("Passwords do not match.", "error")
            return render_template("register.html")

        
        existing_user = User.query.filter_by(username=username).first()

        if existing_user:
            flash("Username already exists.", "error")
            return render_template("register.html")

        
        hashed_password = generate_password_hash(password)

        
        new_user = User(
            username=username,
            password=hashed_password
        )

        
        db.session.add(new_user)
        db.session.commit()

        flash("Account created successfully! Please login.", "success")

        return redirect(url_for("auth.login"))

    return render_template("register.html")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home"))

    if request.method == "POST":

        username = request.form.get("username", "").strip()
        password = request.form.get("password")

        user = User.query.filter_by(username=username).first()

        if not user:
            flash("Invalid username or password.", "error")
            return render_template("login.html")
        if not check_password_hash(user.password, password):
            flash("Invalid username or password.", "error")
            return render_template("login.html")
        login_user(user)
        return redirect(url_for("home"))

    return render_template("login.html")

@auth_bp.route("/logout")
@login_required
def logout():

    logout_user()

    return redirect(url_for("auth.login"))