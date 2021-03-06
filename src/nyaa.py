import requests
import xmltodict
import json
import collections

class Nyaa:
    '''
     Makes a search query to nyaa.si with the given keyword that returns a
     RSS file converted into a dictionary that we can use.
    '''

    def search(keyword):
        nyaa_baseurl = "https://nyaa.si/?page=rss&c=1_0&f=0&q="

        request  = requests.get(nyaa_baseurl + keyword)
        response = xmltodict.parse(request.text)

        results = []

        try:
            if type(response['rss']['channel']['item']) is collections.OrderedDict:
                results.append(response['rss']['channel']['item'])
            else:
                results = response['rss']['channel']['item']

        except KeyError as ex:
            results = []

        return results

class NyaaPantsu:
    '''
     Makes a search query to nyaa.pantsu.cat with the given keyword that returns a
     RSS file converted into a dictionary that we can use.
    '''

    def search(keyword):
        nyaa_baseurl = "https://nyaa.pantsu.cat/feed?c=_&s=0&max=99999&userID=0&q="

        request  = requests.get(nyaa_baseurl + keyword)
        response = xmltodict.parse(request.text)

        results = []

        try:
            if type(response['rss']['channel']['item']) is collections.OrderedDict:
                results.append(response['rss']['channel']['item'])
            else:
                results = response['rss']['channel']['item']

        except KeyError as ex:
            results = []

        return results
