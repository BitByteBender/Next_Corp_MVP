#!/usr/bin/python3

from flask import Blueprint, render_template, redirect, url_for, flash, request, session
import requests


employee_login = Blueprint('employee_login', __name__, template_folder='templates', static_folder='../static')
api_url = 'http://localhost:5000/api/employees'


@employee_login.route('/employee_login/', methods=['GET', 'POST'], strict_slashes=False)
def login_page():
    if request.method == 'POST':
        employee_id = request.form.get('employee_id')
        password = request.form.get('password')

        if not employee_id or not password:
            flash("All fields are required!")
            return redirect(url_for('employee_login.login_page'))

        if authenticate_employee(employee_id, password):
            flash("Login successful!")
            session['employee_id'] = employee_id
            employee_data = get_employee_data(employee_id)
            if employee_data:
                session['employee_name'] = employee_data['name']
                print(f"[Login Page] Set Employee Name in session: {session['employee_name']}")
                print(f"[Login Page] Full session after setting employee name: {session.items()}")
            else:
                flash("Failed to retrieve employee data.")
                return redirect(url_for('employee_login.login_page'))
            return redirect(url_for('home_page'))
        else:
            flash("Invalid Credentials.")
            return redirect(url_for('employee_login.login_page'))

    return render_template('employee_login.html')


def authenticate_employee(employee_id, password):
    try:
        response = requests.get(f"{api_url}/{employee_id}")
        if response.status_code == 200:
            employee_data = response.json()
            print("[Login Page] Employee data retrieved: ", employee_data)
            print(f"[Login Page] Input password: {password}, Stored password: {employee_data['passwd']}")

            if employee_data['passwd'] == password:
                print("[Login Page] Password match successful!")
                return True
            else:
                print("[Login Page] Password does not match.")
        else:
            print("[Login Page] Failed to retrieve employee data.")
        return False
    except requests.exceptions.RequestException as e:
        flash(f"Error: {str(e)}")
        return False


def get_employee_data(employee_id):
    try:
        response = requests.get(f"{api_url}/{employee_id}")
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except requests.exceptions.RequestException as e:
        flash(f"Error: {str(e)}")
        return None
