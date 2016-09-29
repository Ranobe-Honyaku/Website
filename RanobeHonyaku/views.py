from kyoukai.response import Response
from kyoukai.context import HTTPRequestContext


from RanobeHonyaku import app
from RanobeHonyaku.utils import setup_file, apps, SITE_NAME


# Our error handlers
# @app.root.errorhandler(404)
# def error_404_not_found(ctx: HTTPRequestContext, e):
#     return ctx.app.render_template("error.html", title=SITE_NAME + stre, setup_file=setup_file, error=e)
#
#
# @app.root.errorhandler(401)
# def error_401_unauthorized(ctx: HTTPRequestContext, e):
#     return ctx.app.render_template("error.html", title=SITE_NAME + e, setup_file=setup_file, error=e)
#
#
# @app.root.errorhandler(500)
# def error_500_server_error(ctx: HTTPRequestContext, e):
#     return ctx.app.render_template("error.html", title=SITE_NAME + e, setup_file=setup_file, error=e)
#
#
# @app.root.errorhandler(403)
# def error_403_forbidden(ctx: HTTPRequestContext, e):
#     return ctx.app.render_template("error.html", title=SITE_NAME + e, setup_file=setup_file, error=e)


# The root of the domain
@app.route("/")
async def index(ctx: HTTPRequestContext):
    return ctx.app.render_template("home.html", title=SITE_NAME + "Home", setup_file=setup_file)


# The route for our page of approved applications
@app.route("/applications")
async def applications(ctx: HTTPRequestContext):
    return ctx.app.render_template("applications.html", setup_file=setup_file, applications=apps)


# The route that redirects to our Github org
@app.route("/api")
async def redirect_to_github(ctx: HTTPRequestContext):
    return Response.redirect(setup_file["SOCIAL"]["GITHUB"])


# The route that leads to the page for main projects
@app.route("/main-projects")
async def main(ctx: HTTPRequestContext):
    return ctx.app.render_template("projects.html", setup_file=setup_file)


# The route that leads to the page for teaser projects
@app.route("/teaser-projects")
async def teasers(ctx: HTTPRequestContext):
    return ctx.app.render_template("projects.html", setup_file=setup_file)

if __name__ == "__main__":
    app.run(ip="127.0.0.1", port=5000)