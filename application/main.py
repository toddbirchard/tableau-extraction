import requests
import xml
import xmltodict
import json
from xml.etree import ElementTree


class ExtractView:
    """Class instance for extracting a single Tableau View."""

    token = ''
    siteID = ''
    namespaces = {
        '@token': 'token',
        '@id': 'id'
     }

    def __init__(self, base_url, username, password, tableau_site):
        """Initialize instance."""
        self.url = base_url
        self.user = username
        self.password = password
        self.sitename = tableau_site

    def get_view(self, view):
        """Get all data contained in a single view."""
        # Authorize using our generated token
        headers = {'X-Tableau-Auth': token}
        r = requests.get(self.url + '/api/3.0/sites/' + self.siteID +'/views/' + view + '/data', auth=(self.user, self.password), headers=headers)
        return r.content

    def get_all_views_in_site(self):
        """List every view contained in a Tableau Site."""
        # Authorize using our generated token
        headers = {'X-Tableau-Auth': token}
        # Execute API request
        r = requests.get(self.url + '/api/3.0/auth/signin', auth=(self.user, self.password), headers=headers)
        result = r.content
        print(result)

    def auth_token(self):
        """Receive Auth token to perform API requests."""
        # Oh great, XML. My favorite.
        headers = {'Content-Type': 'application/xml'}
        # Pass your username, password, and Tableau "site" name
        body = '<tsRequest><credentials name="'+ self.user + '" password="'+ self.password + '" ><site contentUrl="' + self.sitename + '" /></credentials></tsRequest>'
        # Execute API request
        r = requests.post(self.url + '/api/3.0/auth/signin', auth=(self.user, self.password), headers=headers, data=body)
        xmltree = ElementTree.fromstring(r.content)
        result = json.dumps(xmltodict.parse(r.content), indent=4)
        clean_dict = {key.strip(): item.strip() for key, item in result.items()}
        self.token = clean_dict['tsResponse']['credentials']['@token']
        self.siteID = clean_dict['tsResponse']['credentials']['site']['@id']
        return result


view = ExtractView('http://charthub.io', 'todd', 'flyeaglesfly', 'Hackers')
view.auth_token()
