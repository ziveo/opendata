import requests
from agol import *


class Connect(object):
    def __init__(self, url, **kwargs):
        self.url = url
        self.testname = "Jon"
        self.is_valid = self.is_valid(self.url, **kwargs)

    def is_valid(self, url):
        try:
            code = requests.get(url).status_code
        except:
            code = 500
        if code != 200:
            raise Exception("Url Not Valid")
        return code


class Data(object):
    def __init__(self, conn, **kwargs):
        self.url = conn.url

    def getDatasetsList(self):
        response = requests.get(self.url)
        if response.headers.get('content-type') == 'application/json; charset=utf-8':
            return response.json()['dataset']
        else:
            return []

    def getDatasetTitle(self, dataset):
        return dataset['title']

    def getDatasetDescription(self, dataset):
        return dataset['description']

    def getDatasetPublisher(self, dataset):
        return dataset['publisher']['name']

    def getDatasetKeywords(self, dataset):
        return dataset['keyword']

    def getDatasetUrl(self, dataset):
        return dataset['landingPage']

    def getDatasetDateIssued(self, dataset):
        return dataset['landingPage']

    def getDatasetDateModified(self, dataset):
        return dataset['modified']

    def getDatasetContact(self, dataset):
        contact_point = dataset['contactPoint']
        contact_email = ''
        contact_name = ''

        if contact_point.has_key('hasEmail'):
            contact_email = contact_point['hasEmail']
        if contact_point.has_key('fn'):
            contact_name = contact_point['fn']
        return contact_name, contact_email

    def getDatasetResources(self, dataset):
        return dataset['distribution']

    def getDatasetSpatial(self, dataset):
        if dataset.has_key('spatial'):
            return dataset['spatial']
        else:
            return None

    def getDatasetTheme(self, dataset):
        return dataset['theme']

    def getDatasetOpenDataID(self, dataset):
        return dataset['identifier'].split('/')[-1]  # .split('_')[0]

    def getDatasetAGOLItem(self, itemID):
        return AgolItem(id=itemID)

    def getDatasetAGOLItemID(self, dataset):
        return dataset['identifier'].split('/')[-1].split('_')[0]

    #
    # OpenDataPortal Resource Functions
    #

    def getResourcesTitle(self, resource):
        name = 'Resource'
        if resource.has_key('title'):
            name = resource['title']
        else:
            name = resource['format']
        return name

    def getResourcesURL(self, resource):
        url = ''
        if resource.has_key('accessURL'):
            url = resource['accessURL']
        elif resource.has_key('accessUrl'):
            url = resource['accessUrl']
        elif resource.has_key('downloadUrl'):
            url = resource['downloadUrl']
        elif resource.has_key('downloadURL'):
            url = resource['downloadURL']
        return url

    def getResourcesMediaType(self, resource):
        return resource['mediaType']

    def getResourcesFormat(self, resource):
        return resource['format']
