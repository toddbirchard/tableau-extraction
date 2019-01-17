from flask import current_app as app
from flask import render_template, Blueprint
from flask_assets import Bundle, Environment
import json
from . import r
from . import tableau

home_blueprint = Blueprint('home', __name__, template_folder='templates', static_folder='static')


assets = Environment(app)
'''js = Bundle('js/bin/*.js', filters='jsmin', output='dist/packed.js')
scss = Bundle('scss/*.scss', 'scss/custom.scss', filters='libsass', output='dist/all.css')
assets.register('scss_all', scss)
assets.register('js_all', js)
scss.build()
js.build()'''


@app.route('/', methods=['GET', 'POST'])
def entry():
    headers = {'Content-Type': 'application/xml'}
    tableau_view_extractor = tableau.ExtractTableauView()
    xml = tableau_view_extractor.initialize_tableau_request()
    print('xml = ', xml)
    token = tableau_view_extractor.get_token(xml)
    print('token = ', token)
    site = tableau_view_extractor.get_site(xml)
    print('site = ', site)
    views = tableau_view_extractor.list_views(site, xml, token)
    print(views)
    return render_template(
        'index.html',
        title="Here are your views.",
        template="home-template",
        views=views
    )

    # view = tableau_view_extractor.get_view(site, xml, '9a4a1de9-b7af-4a4a-8556-fd5ac82f92bd', token)
