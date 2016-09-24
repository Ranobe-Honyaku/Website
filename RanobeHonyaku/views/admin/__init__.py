from flask import Blueprint, render_template

from utils import setup_file

admin = Blueprint("admin", __name__, url_prefix="/admin")


@admin.route(rule="")
def dashboard():
    return render_template("admin/dashboard.html", setup_file=setup_file)
