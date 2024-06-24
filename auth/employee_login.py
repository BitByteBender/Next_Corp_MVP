#!/usr/bin/python3

from flask import Blueprint, render_template, redirect, url_for, flash, request, session
import requests


employee_login = Blueprint('employee_login', __name__, template_folder='templates', static_folder='../static')
api_url = 'http://localhost:5000/api/employees'


@employee_login.route('/employee_login/', methods=['GET', 'POST'], strict_slashes=False)
def login_page():
    """
    Retrieve form data
    Check if any field is missing
    Authenticate the employee using employee_id and password
    Redirect to a profile or check-in page after successful login
    Returns the login page template
    """
    if request.method == 'POST':
        employee_id = request.form.get('employee_id')
        password = request.form.get('password')

        if not employee_id or not password:
            flash("All fields are required!")
            return redirect(url_for('employee_login.login_page'))

        if authenticate_employee(employee_id, password):
            flash("Login successful!")
            session['employee_id'] = employee_id
            session['employee_name'] = get_employee_data(employee_id)['name']
            return redirect(url_for('home.home_page'))
        else:
            flash("Invalid Credentials.")
            return redirect(url_for('employee_login.login_page'))

    return render_template('employee_login.html')


def authenticate_employee(employee_id, password):
    """
    Function to authenticate the employee
    Check if the password matches
    """
    try:
        response = requests.get(f"{api_url}/{employee_id}")
        if response.status_code == 200:
            employee_data = response.json()
            print("Employee data retrieved: ", employee_data)
            print(f"Input password: {password}, Stored password: {employee_data['passwd']}")

            if employee_data['passwd'] == password:
                print("Password match successful!")
                return True
            else:
                print("Password does not match.")
        else:
            print("Failed to retrieve employee data.")
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
