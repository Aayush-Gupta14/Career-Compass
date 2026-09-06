from flask import Blueprint, render_template, request, redirect, url_for
from models import db, Problem
from flask_login import login_required, current_user


dsa_bp = Blueprint("dsa", __name__)

@dsa_bp.route("/dsa", methods=["GET", "POST"])
@login_required
def dsa():

    if request.method == "POST":

        problem = Problem(
            name=request.form["problem_name"],
            platform=request.form["platform"],
            difficulty=request.form["difficulty"],
            topic=request.form["topic"],
            status=request.form["status"],
            notes=request.form["notes"],
            user_id=current_user.id
        )
        db.session.add(problem)
        db.session.commit()

        return redirect(url_for("dsa.dsa"))

    problems = Problem.query.filter_by(user_id=current_user.id).all()

    total = Problem.query.filter_by(user_id=current_user.id).count()
    solved = Problem.query.filter_by(user_id=current_user.id,status="Solved").count()
    easy = Problem.query.filter_by(user_id=current_user.id,difficulty="Easy").count()
    medium = Problem.query.filter_by(user_id=current_user.id,difficulty="Medium").count()

    hard = Problem.query.filter_by(user_id=current_user.id,difficulty="Hard").count()

    return render_template(
        "dsa.html",
        problems=problems,
        total=total,
        solved=solved,
        easy=easy,
        medium=medium,
        hard=hard
    )
@dsa_bp.route("/delete/<int:id>")
@login_required
def delete_problem(id):

    problem = Problem.query.filter_by(id=id,user_id=current_user.id).first_or_404()

    db.session.delete(problem)
    db.session.commit()

    return redirect(url_for("dsa.dsa"))

@dsa_bp.route("/solve/<int:id>")
@login_required
def solve_problem(id):

    problem = Problem.query.filter_by(id=id,user_id=current_user.id).first_or_404()

    problem.status = "Solved"

    db.session.commit()

    return redirect(url_for("dsa.dsa"))

