#!/usr/bin/python3

from flask import Blueprint, render_template, redirect, url_for, flash, request
import requests

login = Blueprint('login', __name__, template_folder='templates')
api_url = 'http://localhost:5000/api/corps'


@login.route('/login/', methods=['GET', 'POST'], strict_slashes=False)
def login_page():
    if request.method == 'POST':
        # Retrieve form data
        corp_id = request.form.get('corp_id')
        password = request.form.get('password')

        # Check if any field is missing
        if not corp_id or not password:
            flash("All fields are required!")
            return redirect(url_for('login.login_page'))

        # Authenticate the corporation using corp_id and password
        if authenticate_corp(corp_id, password):
            flash("Login successful!")
            # Redirect to a dashboard or home page after successful login
            return redirect(url_for('dashboard.dashboard'))
        else:
            flash("Invalid Credentials.")
            return redirect(url_for('login.login_page'))

    # Render the login page template
    return render_template('login.html')

# Function to authenticate the corporation
def authenticate_corp(corp_id, password):
    try:
        response = requests.get(f"{api_url}/{corp_id}")
        if response.status_code == 200:
            corp_data = response.json()
            # Check if the password matches
            if corp_data['passwd'] == password:
                return True
        return False
    except requests.exceptions.RequestException as e:
        flash(f"Error: {str(e)}")
        return False
