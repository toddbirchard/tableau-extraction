import requests
import xml.etree.ElementTree as ET
from . import r
import pandas as pd
import io


class ExtractTableauView:
    """Class for working in a Tableau instance."""

    __baseurl = r.get('baseurl')
    __username = r.get('username')
    __password = r.get('password')
    __database = r.get('uri')
    __contenturl = r.get('contenturl')

    @classmethod
    def get_view(cls, site, xml, view, token):
        """Extract contents of a single view."""
        headers = {'X-Tableau-Auth': token,
                   'Content-Type': 'text/csv'
                   }
        req = requests.get(cls.__baseurl + '/api/3.2/sites/' + str(site) +'/views/' + str(view) + '/data',
                           headers=headers,
                           stream=True)
        csv_text = req.text
        view_df = pd.read_csv(io.StringIO(csv_text), header=0)
        return view_df

    @classmethod
    def list_sites(cls, token):
        """Get all sites belonging to a Tableau Instance."""
        headers = {'X-Tableau-Auth': token}
        req = requests.get(cls.__baseurl + '/api/3.2/sites', headers=headers)
        root = ET.fromstring(req.content)
        sites_arr = []
        for child in root.iter('*'):
            if child.tag == '{http://tableau.com/api}sites':
                for site in child:
                    site_dict = {
                        'name': site.attrib.get('name'),
                        'id': site.attrib.get('id'),
                        'contentURL': site.attrib.get('contentUrl'),
                        'state': site.attrib.get('state')
                    }
                    sites_arr.append(site_dict)
        return sites_arr

    @classmethod
    def list_views(cls, site, xml, token):
        """List all views belonging to a Tableau Site."""
        headers = {'X-Tableau-Auth': token}
        req = requests.get(cls.__baseurl + '/api/3.2/sites/' + site + '/views',
                           auth=(cls.__username, cls.__password),
                           headers=headers)
        root = ET.fromstring(req.content)
        views_arr = []
        for child in root.iter('*'):
            if child.tag == '{http://tableau.com/api}views':
                for view in child:
                    view_dict = {
                        'name': view.attrib.get('name'),
                        'id': view.attrib.get('id'),
                        'url': cls.__baseurl + '/' + view.attrib.get('contentUrl'),
                        'created': view.attrib.get('createdAt'),
                        'updated': view.attrib.get('updatedAt')
                    }
                    views_arr.append(view_dict)
        return views_arr

    @classmethod
    def get_token(cls, xml):
        """Receive Auth token to perform API requests."""
        for child in xml.iter('*'):
            if child.tag == '{http://tableau.com/api}credentials':
                token = child.attrib.get('token')
                return token

    @classmethod
    def get_site(cls, xml, key):
        """Retrieve ID of Tableau 'site' instance."""
        root = xml
        for child in root.iter('*'):
            if child.tag == '{http://tableau.com/api}site':
                site = child.attrib.get(key)
                return site

    @classmethod
    def initialize_tableau_request(cls):
        """Retrieve core XML for interacting with Tableau."""
        headers = {'Content-Type': 'application/xml'}
        body = '<tsRequest><credentials name="' \
               + cls.__username \
               + '" password="' \
               + cls.__password \
               + '" ><site contentUrl="'\
               + cls.__contenturl \
               + '" /></credentials></tsRequest>'
        req = requests.post(cls.__baseurl + '/api/3.2/auth/signin',
                            auth=(cls.__username, cls.__password),
                            headers=headers,
                            data=body)
        root = ET.fromstring(req.content)
        return root
