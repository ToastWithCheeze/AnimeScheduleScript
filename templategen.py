import requests
import json


baseurl = 'https://animeschedule.net/api/v3/'

endpoint = 'anime/'


print("Enter Anime: ")
anime = input()

animeresult = anime.replace(' ', '-')

api = baseurl + endpoint + animeresult

response = requests.get(api)

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json())