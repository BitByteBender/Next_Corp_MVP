#!/usr/bin/env python3

from flask import Flask, jsonify, render_template, url_for
from models import storage, initialize_storage
from api.views import app_views
from os import getenv
from pages import view
from auth.register import register
from auth.login import login
from dashboard import dash
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = getenv('SECRET_KEY', os.urandom(24))

initialize_storage()
storage_instance = storage

app.register_blueprint(app_views)
app.register_blueprint(view)
app.register_blueprint(register, url_prefix='/corp_auth')
app.register_blueprint(login, url_prefix='/corp_auth')
app.register_blueprint(dash, url_prefix='/admin')

@app.errorhandler(404)
def trigger_error(err):
    return jsonify({"error": "Not found"}), 404

@app.teardown_appcontext
def teardown_db(exception):
    if storage_instance:
        storage_instance.close()

if __name__ == '__main__':
    host = getenv('NC_API_HOST', '0.0.0.0')
    port = int(getenv('NC_API_PORT', '5000'))
    app.run(host=host, port=port, threaded=True, debug=True)
