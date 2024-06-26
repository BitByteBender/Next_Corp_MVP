#!/usr/bin/python3

from flask import Blueprint, redirect, url_for, flash, session, jsonify

logout = Blueprint('logout', __name__, static_folder='../static')


@logout.route('/logout/', methods=['GET'], strict_slashes=False)
def logout_usr():
    """
    Logout the user and clear session data.
    Redirect to login page.
    """
    session.clear()
    flash("You have been logged out.", 'info')
    return jsonify({"message": "logout successful"}), 200
