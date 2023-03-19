import pandas as pd
from flask import Blueprint, Markup
from flask import current_app as app
from flask import render_template, request
from flask_assets import Bundle, Environment

from . import database, tableau

home_blueprint = Blueprint(
    "home", __name__, template_folder="templates", static_folder="static"
)

assets = Environment(app)
js = Bundle("js/*.js", filters="jsmin", output="dist/packed.js")
scss = Bundle("scss/*.scss", filters="libsass", output="dist/all.css")
assets.register("scss_all", scss)
assets.register("js_all", js)
scss.build(force=True, disable_cache=True)
js.build(force=True, disable_cache=True)


@home_blueprint.route("/nav.html", methods=["GET"])
def nav():
    """Build nav before every template render."""
    tableau_view_extractor = tableau.ExtractTableauView()
    xml = tableau_view_extractor.initialize_tableau_request()
    token = tableau_view_extractor.get_token(xml)
    all_sites = tableau_view_extractor.list_sites(token)
    return render_template("nav.html", all_sites=all_sites)


@home_blueprint.route("/", methods=["GET", "POST"])
def entry():
    """Homepage which lists all available views."""
    tableau_view_extractor = tableau.ExtractTableauView()
    xml = tableau_view_extractor.initialize_tableau_request()
    token = tableau_view_extractor.get_token(xml)
    site_id = tableau_view_extractor.get_site(xml, "id")
    site_name = tableau_view_extractor.get_site(xml, "contentUrl")
    views = tableau_view_extractor.list_views(site_id, xml, token)
    all_sites = tableau_view_extractor.list_sites(token)
    site = tableau_view_extractor.get_site(xml)
    return render_template(
        "index.html",
        title="Here are your views.",
        template="home-template",
        views=views,
        token=token,
        xml=xml,
        site_name=site_name,
        site=site,
        all_sites=all_sites,
    )


@home_blueprint.route("/view", methods=["GET", "POST"])
def view():
    """Display a preview of a selected view."""
    site = request.args.get("site")
    xml = request.args.get("xml")
    view = request.args.get("view")
    token = request.args.get("token")
    tableau_view_extractor = tableau.ExtractTableauView()
    view_df = tableau_view_extractor.get_view(site, xml, view, token)
    view_df.to_csv("application/static/data/view.csv")
    return render_template(
        "view.html",
        title="Your View",
        template="home-template",
        view=view,
        token=token,
        xml=xml,
        site=site,
        view_df=Markup(view_df.to_html(index=False)),
    )


@home_blueprint.route("/export", methods=["GET", "POST"])
def export():
    """Export view to external database."""
    view_df = pd.read_csv("application/static/data/view.csv")
    view_df.to_sql(
        name="temp",
        con=database.engine,
        if_exists="replace",
        chunksize=50,
        index=True,
    )
    return render_template(
        "export.html",
        title="Success!",
        template="success-template",
    )
