#!/usr/bin/env python3

from flask import Flask, jsonify, render_template
from models import storage
from api.views import app_views
import os
from os import getenv
from pages import view
from auth.register import register
from auth.login import login
from auth.logout import logout
from auth.reset_password import reset
from dashboard import dash


app = Flask(__name__)
app.config['SECRET_KEY'] = getenv('SECRET_KEY', os.urandom(24))


app.register_blueprint(app_views)
app.register_blueprint(view)
app.register_blueprint(register, url_prefix='/corp_auth')
app.register_blueprint(login, url_prefix='/corp_auth')
app.register_blueprint(reset, url_prefix='/corp_auth')
app.register_blueprint(dash, url_prefix='/admin')
app.register_blueprint(logout, url_prefix='/auth')


@app.errorhandler(404)
def trigger_error(err):
    """ Triggers a 404 error """
    return (jsonify({"error": "Not found"}), 404)


@app.teardown_appcontext
def teardown_db(exception):
    """ Close storage on teardown """
    storage.close()


if __name__ == '__main__':
    """ Runs flask app on a specified adr and port """
    host = getenv('NC_API_HOST', '0.0.0.0')
    port = int(getenv('NC_API_PORT', '5000'))
    app.run(host=host, port=port, threaded=True, debug=True)
