from os.path import abspath, normpath, join
from dash import Dash
import dash_table
from flask import Blueprint, request
from dash.dependencies import Input, State, Output
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from . import tableau
import csv
from csv import reader

view_blueprint = Blueprint('view_blueprint', __name__, template_folder='templates', static_folder='static')
df = pd.DataFrame(data=['0', '1', '2'])


def Add_Dash(server):
    """Populates page with all available dataframes."""
    external_scripts = ['https://code.jquery.com/jquery-3.3.1.min.js','https://temp.sfo2.digitaloceanspaces.com/df_titles4.js']
    external_stylesheets = ['https://temp.sfo2.digitaloceanspaces.com/all15.css']

    dash_app = Dash(server=server, url_base_pathname='/data/', external_scripts=external_scripts, external_stylesheets=external_stylesheets)

    # stylesheet = p.glob('application/static/dist/*.css')
    # dash_app.css.append_css({"external_url": "https://temp.sfo2.digitaloceanspaces.com/all12.css"})

    # Create layout
    dash_app.layout = html.Div(
        # get_table(df),
        id='flex-container'
        )
    return dash_app.server


@view_blueprint.route('/view', methods=['GET', 'POST'])
def view():
    """Gets all CSVS in datasets directory."""
    data_filepath = 'application/static/data/view.csv'
    df = pd.read_csv('application/static/data/view.csv')
    table_preview = html.Div([dash_table.DataTable(
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict("rows"),
        sorting=True,
        style_table={}
    )], id=str('application/data/view.csv'))
