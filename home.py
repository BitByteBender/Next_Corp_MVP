#!/usr/bin/python3

from flask import Blueprint, render_template, session, redirect, url_for, flash
from employee_profile import get_employee_name

home = Blueprint('home', __name__, template_folder='templates', static_folder='../static')


@home.route('/')
def home_page():
    if 'employee_id' not in session:
        flash("You need to log in first.")
        return redirect(url_for('employee_login.login_page'))

    employee_id = session['employee_id']
    employee_name = get_employee_name(employee_id)

    if not employee_name:
        flash("Failed to retrieve employee data.")
        return redirect(url_for('employee_login.login_page'))

    return render_template('home.html', employee_name=employee_name, employee_id=employee_id)
