import requests
import bs4
from apiverification import api

# Send request to server
def main_request():
    r = requests.get(api)
    return r.json()

data = main_request()

# Stuff
native = data['names']['native']
synomyms = data['names']['synonyms']
description = data['description']
anilist = data['websites']['aniList']

parserDesc = bs4.BeautifulSoup(description, "html.parser")
outputDescription = parserDesc.get_text()

# Output
print('Title: ' + native + " " + str(synomyms))

print('Description \n' + outputDescription)

print('\nGenres:\n')
for genres in data['genres']:
    print(genres['name'])

print('\nWebsites: ' + anilist)
