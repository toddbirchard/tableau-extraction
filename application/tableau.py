import requests
import json
import xml.etree.ElementTree as ET
from . import r
import tableauserverclient as TSC


class ExtractTableauView:
    """Class instance for extracting a single Tableau View."""

    __baseurl = r.get('baseurl')
    __username = r.get('username')
    __password = r.get('password')
    __database = r.get('uri')
    __contenturl = r.get('contenturl')
    __tableau_auth = TSC.TableauAuth(r.get('username'), r.get('password'))
    __server = TSC.Server(r.get('baseurl'))

    @classmethod
    def get_all_views(cls):
        with cls.__server.auth.sign_in(cls.__tableau_auth):
            all_views, pagination_item = cls.__server.views.get()
            view_arr = [view.name for view in all_views]
            view_ids = [view.id for view in all_views]
            view_dict = dict(zip(view_arr, view_ids))
            print(view_dict)
            return view_dict

    @classmethod
    def get_view(cls, site, xml, view, token):
        """Get contents of a single view."""
        headers = {'X-Tableau-Auth': token,
                   'Content-Type': 'application/x-www-form-urlencoded'
                   }
        req = requests.get(cls.__baseurl + '/api/3.2/sites/' + str(site) +'/views/' + str(view) + '/data', headers=headers)
        print(req.content)
        return req.content

    @classmethod
    def list_views(cls, site, xml, token):
        """Get all views belonging to a Tableau Site."""
        headers = {'X-Tableau-Auth': token}
        req = requests.get(cls.__baseurl + '/api/3.2/sites/' + site + '/views', auth=(cls.__username, cls.__password), headers=headers)
        root = ET.fromstring(req.content)
        views_arr = []
        for child in root.iter('*'):
            if child.tag == '{http://tableau.com/api}views':
                for view in child:
                    view_dict = {
                        'name': view.attrib.get('name'),
                        'id': view.attrib.get('id')
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
    def get_site(cls, xml):
        """Retrieve ID of Tableau site instance."""
        root = xml
        for child in root.iter('*'):
            if child.tag == '{http://tableau.com/api}site':
                site = child.attrib.get('id')
                return site

    @classmethod
    def initialize_tableau_request(cls):
        """Retrieve core XML for interacting with Tableau."""
        headers = {'Content-Type': 'application/xml'}
        # Pass your username, password, and Tableau "site" name
        body = '<tsRequest><credentials name="' + cls.__username + '" password="' + cls.__password + '" ><site contentUrl="' + cls.__contenturl + '" /></credentials></tsRequest>'
        # Execute API request
        req = requests.post(cls.__baseurl + '/api/3.2/auth/signin', auth=(cls.__username, cls.__password), headers=headers, data=body)
        root = ET.fromstring(req.content)
        return root


'''tableau_view_extractor = ExtractTableauView()
xml = tableau_view_extractor.initialize_tableau_request()
print('xml = ', xml)
token = tableau_view_extractor.get_token(xml)
print('token = ', token)
site = tableau_view_extractor.get_site(xml)
print('site = ', site)
views = tableau_view_extractor.list_views(site, xml, token)
print('views = ', views)'''
