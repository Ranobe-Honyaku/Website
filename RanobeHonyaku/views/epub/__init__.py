from flask import Blueprint

epub = Blueprint("epub", __name__, subdomain="epub")


@epub.route(rule="/")
def root():
    return render_template("epub/epub_generator.html")
