import urllib.request, urllib.parse, urllib.error
import json

def molar_mass(element):
    url = "https://api.apiverve.com/v1/periodictable?name=" + element
    headers = {
        "x-api-key": "4c182626-58fd-4c98-94f0-77f0bf1ca0cd"
    }


molar_mass('hydrogen')
