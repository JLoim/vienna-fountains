def main():
    import fetch
    import json
    import argparse

    with open('fountains.json', "r") as fountains:
        data = json.load(fountains)
    #Making sure users have to submit lat and longitude    
    parser = argparse.ArgumentParser()
    parser.add_argument('--lat', type=float, required=True, help="Latitude of the location")
    parser.add_argument('--lon', type=float, required=True, help="Longitude of the location")
    args = parser.parse_args()





# To protect against argparse errors
if __name__ == "__main__":
    main()