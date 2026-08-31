from fetch import fetch_fountains 
import json
import argparse
import distance
from fountains import Fountain 
def main(): 
    with open('fountains.json', "r") as fountains:
        data = json.load(fountains)
    #Making sure users have to submit lat and longitude    
    parser = argparse.ArgumentParser()
    parser.add_argument('--lat', type=float, required=True, help="Latitude of the location")
    parser.add_argument('--lon', type=float, required=True, help="Longitude of the location")
    args = parser.parse_args()

    # Convert JSON into list then sort by distance to user input
    fountains_list = []
    for each in data['features']:
        properties = each['properties']
        coordinates = each['geometry']['coordinates'] # Order is [lon,lat]
        fountain = Fountain(
            properties['OBJECTID'], 
            coordinates[1], 
            coordinates[0], 
            properties['BASIS_TYP'], 
            properties['BASIS_TYP_TXT']
        )
        haversine_distance = distance.haversine(args.lon, args.lat, fountain.lon, fountain.lat)

        fountains_list.append((fountain, haversine_distance))
        fountains_list.sort(key=lambda x: x[1]) # Sort by distance)
        fountains_list = fountains_list[:5] # Get the 5 closest fountains
    print(fountains_list)



# To protect against argparse errors
if __name__ == "__main__":
    main()