from kyoukai.context import HTTPRequestContext
from kyoukai.response import Response

from RanobeHonyaku.utils import setup_file, apps
from RanobeHonyaku import app


# Our error handlers
# @app.errorhandler(404)
# def error_404_not_found(e):
#     return render_template("error.html", setup_file=setup_file, error=e)


# @app.errorhandler(401)
# def error_401_unauthorized(e):
#     return render_template("error.html", setup_file=setup_file, error=e)


# @app.errorhandler(500)
# def error_500_server_error(e):
#     return render_template("error.html", setup_file=setup_file, error=e)


# @app.errorhandler(403)
# def error_403_forbidden(e):
#     return render_template("error.html", setup_file=setup_file, error=e)


# The root of the domain
@app.route("/")
async def index(ctx: HTTPRequestContext):
    return ctx.app.render_template("home.html", setup_file=setup_file)


# The route for our page of approved applications
@app.route("/applications")
async def applications(ctx: HTTPRequestContext):
    return app.render_template("applications.html", setup_file=setup_file, applications=apps)


# The route that redirects to our Github org
@app.route("/api")
async def redirect_to_github(ctx: HTTPRequestContext):
    return Response.redirect(setup_file["SOCIAL"]["GITHUB"])


# The route that leads to the page for main projects
@app.route("/main-projects")
async def main(ctx: HTTPRequestContext):
    return app.render_template("projects.html", setup_file=setup_file)


# The route that leads to the page for teaser projects
@app.route("/teaser-projects")
async def teasers(ctx: HTTPRequestContext):
    return app.render_template("projects.html", setup_file=setup_file)
