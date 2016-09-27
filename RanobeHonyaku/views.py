from flask import render_template, redirect

from RanobeHonyaku.utils import setup_file, apps
from RanobeHonyaku import app


# Our error handlers
@app.errorhandler(404)
def error_404_not_found(e):
    return render_template("error.html", setup_file=setup_file, error=e)


@app.errorhandler(401)
def error_401_unauthorized(e):
    return render_template("error.html", setup_file=setup_file, error=e)


@app.errorhandler(500)
def error_500_server_error(e):
    return render_template("error.html", setup_file=setup_file, error=e)


@app.errorhandler(403)
def error_403_forbidden(e):
    return render_template("error.html", setup_file=setup_file, error=e)


# The root of the domain
@app.route("/")
def index():
    return render_template("home.html", setup_file=setup_file)


# The route for our page of approved applications
@app.route("/applications")
def applications():
    return render_template("applications.html", setup_file=setup_file, applications=apps)


# The route that redirects to our Github org
@app.route("/api")
def redirect_to_github():
    return redirect(setup_file["SOCIAL"]["GITHUB"], 301)


# The route that leads to the page for main projects
@app.route("/main-projects")
def main():
    return render_template("projects.html", setup_file=setup_file)


# The route that leads to the page for teaser projects
@app.route("/teaser-projects")
def teasers():
    return render_template("projects.html", setup_file=setup_file)