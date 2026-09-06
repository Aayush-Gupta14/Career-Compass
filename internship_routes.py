from flask import Blueprint, render_template, request, redirect, url_for
from models import db, Internship
from flask_login import login_required, current_user
internship_bp = Blueprint("internship", __name__)


@internship_bp.route("/internship", methods=["GET", "POST"])
@login_required
def internship():

    if request.method == "POST":

        internship = Internship(
            company=request.form["company"],
            role=request.form["role"],
            location=request.form["location"],
            link=request.form["link"],
            application_date=request.form["application_date"],
            deadline=request.form["deadline"],
            status=request.form["status"],
            notes=request.form["notes"],
            user_id=current_user.id
        )

        db.session.add(internship)
        db.session.commit()

        return redirect(url_for("internship.internship"))


    internships = Internship.query.filter_by(user_id=current_user.id).all()

    total = Internship.query.filter_by(user_id=current_user.id).count()

    interviews = Internship.query.filter_by(user_id=current_user.id,status="Interview").count()
    offers = Internship.query.filter(Internship.user_id == current_user.id,Internship.status.in_(["Offer", "Accepted"])).count()
    rejected = Internship.query.filter_by(user_id=current_user.id,status="Rejected").count()
    return render_template(
        "internship.html",
        internships=internships,
        total=total,
        interviews=interviews,
        offers=offers,
        rejected=rejected
    )

@internship_bp.route("/internship/delete/<int:id>")
@login_required
def delete_internship(id):

    internship = Internship.query.filter_by(id=id,user_id=current_user.id).first_or_404()

    db.session.delete(internship)
    db.session.commit()

    return redirect(url_for("internship.internship"))

@internship_bp.route("/internship/status/<int:id>")
@login_required
def next_status(id):

    internship = Internship.query.filter_by(id=id,user_id=current_user.id).first_or_404()
    status_flow = [
        "Applied",
        "OA Scheduled",
        "Interview",
        "Offer",
        "Accepted"
    ]

    if internship.status in status_flow:

        current_index = status_flow.index(internship.status)

        if current_index < len(status_flow) - 1:
            internship.status = status_flow[current_index + 1]

            db.session.commit()

    return redirect(url_for("internship.internship"))