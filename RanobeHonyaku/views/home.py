from flask import Blueprint, render_template

from utils import setup_file, apps

home = Blueprint("home", __name__)

# The root of the domain
@home.route(rule="/")
def index():
    return render_template("home.html", setup_file=setup_file)

# The route for our page of approved applications
@home.route(rule="/applications")
def applications():
    return render_template("applications.html", setup_file=setup_file, applications=apps)
