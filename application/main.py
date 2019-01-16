import requests
import json
import xml.etree.ElementTree as ET
from . import r


class ExtractTableauView:
    """Class instance for extracting a single Tableau View."""

    __baseurl = r.get('baseurl')
    __username = r.get('username')
    __password = r.get('password')
    __database = r.get('uri')

    def __init__(self, base_url, username, password, tableau_site):
        """Initialize Taleau site instance for pillaging sequence."""
        self.url = base_url
        self.user = username
        self.password = password
        self.sitename = tableau_site
        self.xml = self.initialize_tableau_request()
        self.token = self.get_token()
        self.site = self.get_site()
        self.views = self.list_views()

    def get_view(self, view):
        """Get contents of a single view."""
        headers = {'X-Tableau-Auth': self.token}
        r = requests.get(self.url + '/api/3.0/sites/' + self.site +'/views/' + view + '/data', auth=(self.user, self.password), headers=headers)
        print(r.content)
        return r.content

    def list_views(self):
        """Get all views belonging to a Tableau Site."""
        headers = {'X-Tableau-Auth': self.token}
        r = requests.get(self.url + '/api/3.0/sites/' + self.site +'/views', auth=(self.user, self.password), headers=headers)
        root = ET.fromstring(r.content)
        views_arr = []
        for child in root.iter('*'):
            if child.tag == '{http://tableau.com/api}views':
                for view in child:
                    views_arr.append(view.attrib.get('id'))
        return views_arr

    def get_token(self):
        """Receive Auth token to perform API requests."""
        for child in self.xml.iter('*'):
            if child.tag == '{http://tableau.com/api}credentials':
                token = child.attrib.get('token')
                return token

    def get_site(self):
        """Retrieve ID of Tableau site instance."""
        for child in self.xml.iter('*'):
            if child.tag == '{http://tableau.com/api}site':
                site = child.attrib.get('id')
                return site

    def initialize_tableau_request(self):
        """Retrieve core XML for interacting with Tableau."""
        headers = {'Content-Type': 'application/xml'}
        # Pass your username, password, and Tableau "site" name
        body = '<tsRequest><credentials name="' + self.user + '" password="' + self.password + '" ><site contentUrl="' + self.sitename + '" /></credentials></tsRequest>'
        # Execute API request
        r = requests.post(self.url + '/api/3.0/auth/signin', auth=(self.user, self.password), headers=headers, data=body)
        root = ET.fromstring(r.content)
        return root


tableau_view_extractor = ExtractTableauView()
tableau_view_extractor.get_view('[ViewIDOfYourChoice')
