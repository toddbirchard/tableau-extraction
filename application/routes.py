from flask import current_app as app
from flask import make_response
import json
from . import r
from . import main


@app.route('/', methods=['GET', 'POST'])
def entry():
    headers = {'Content-Type': 'application/xml'}
    token = main.auth_token()
    print(token)
    return make_response(str(token), 200, headers)
