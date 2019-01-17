from flask import current_app as app
from flask import render_template, Blueprint, make_response, request, redirect
from flask_assets import Bundle, Environment
import json
from . import r
from . import tableau
import csv
import pandas as pd

home_blueprint = Blueprint('home', __name__, template_folder='templates', static_folder='static')


assets = Environment(app)
js = Bundle('js/*.js', filters='jsmin', output='dist/packed.js')
scss = Bundle('scss/*.scss', filters='libsass', output='dist/all.css')
assets.register('scss_all', scss)
assets.register('js_all', js)
scss.build()
js.build()


@home_blueprint.route('/', methods=['GET', 'POST'])
def entry():
    headers = {'Content-Type': 'application/xml'}
    tableau_view_extractor = tableau.ExtractTableauView()
    xml = tableau_view_extractor.initialize_tableau_request()
    token = tableau_view_extractor.get_token(xml)
    site = tableau_view_extractor.get_site(xml)
    views = tableau_view_extractor.list_views(site, xml, token)
    return render_template(
        'index.html',
        title="Here are your views.",
        template="home-template",
        views=views,
        token=token,
        xml=xml,
        site=site
    )


@home_blueprint.route('/view', methods=['GET', 'POST'])
def view():
    site = request.args.get('site')
    xml = request.args.get('xml')
    view = request.args.get('view')
    token = request.args.get('token')
    tableau_view_extractor = tableau.ExtractTableauView()
    data_filepath = 'application/static/data/view.csv'
    view = tableau_view_extractor.get_view(site, xml, view, token).decode('utf-8')
    # view = view.split("\n")
    with open(data_filepath, "w") as file:
        writer = csv.writer(file)
        for row in view:
            row = row.replace('\""', '')
            row = row.replace("\''", '')
            writer.writerow(str(row))
    return render_template(
        'view.html',
        title="Here are your views.",
        template="home-template",
        view=view
    )
