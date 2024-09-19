from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from models import db, WorkHour

routes = Blueprint('routes', __name__)

@routes.route('/')
@login_required
def home():
    # Get the user's logged work hours
    work_hours = WorkHour.query.filter_by(user_id=current_user.id).all()
    return render_template('index.html', work_hours=work_hours)

@routes.route('/submit_hours', methods=['POST'])
@login_required
def submit_hours():
    date = request.form['date']
    hours = request.form['hours']
    description = request.form['description']  # Include description
    work_hour = WorkHour(user_id=current_user.id, date=date, hours=hours, description=description)
    db.session.add(work_hour)
    db.session.commit()
    return redirect(url_for('routes.home'))  # Redirect to home after submission
