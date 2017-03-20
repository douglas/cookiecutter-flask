from flask import Blueprint, render_template

blueprint = Blueprint(
    "public",
    __name__,
    static_folder='../static',
    template_folder='templates'
)


@blueprint.route("/", methods=["GET"])
def index():
    return render_template("index.jinja")
