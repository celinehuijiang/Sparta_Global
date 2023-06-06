import requests
import json
import pymongo

# connecting to the new database
client = pymongo.MongoClient()
# creating a new database 
db = client['starship']
starships_collection = db['starships']
characters_collection = db['characters']

# API endpoint for starships
url = "https://swapi.dev/api/starships/"

# send GET request to retrieve starship data
response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    # iterate through pages of starship data
    while True:
        # process each starship on the current page
        for starship in data['results']:
            print(starship)

            # Fetch pilot data
            pilots_urls = starship['pilots']
            pilots_object_ids = []

            for pilot_url in pilots_urls:
                pilot_response = requests.get(pilot_url)
                if pilot_response.status_code == 200:
                    pilot_data = pilot_response.json()
                    pilot_object_id = characters_collection.insert_one(pilot_data).inserted_id
                    pilots_object_ids.append(pilot_object_id)

            # peplace "pilots" field with ObjectIDs
            starship['pilots'] = pilots_object_ids

            # insert starship into starships collection
            starships_collection.insert_one(starship)

        # check if there are more pages to fetch
        if data['next'] is not None:
            response = requests.get(data['next'])
            data = response.json()
        else:
            break

    print("Starship data imported successfully.")
else:
    print("Error occurred while retrieving starship data.")



