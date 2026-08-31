import requests
import json

def fetch_fountains():
    r = requests.get('https://data.wien.gv.at/daten/geo?service=WFS&request=GetFeature&version=1.1.0&typeName=ogdwien:TRINKBRUNNENOGD&srsName=EPSG:4326&outputFormat=json')
    with open('fountains.json', "w") as fountains:
        json.dump(r.json(),fountains, ensure_ascii=False, indent=4)
