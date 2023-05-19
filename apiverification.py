import requests

# Stuff needed to get from api
baseurl = 'https://animeschedule.net/api/v3/'

endpoint = 'anime/'

# Input anime name and replaces space with - 
print("Enter Anime: ")
anime = input()

animeresult = anime.replace(' ', '-')

# Combine all the variables above to a single variable
api = baseurl + endpoint + animeresult

response = requests.get(api)
# Checks if the api link is valid or not
if response.status_code == 200:
    print('Request Successful\n')
    
elif response.status_code == 404:
    print('Not found')
    exit()
else:
    print('Error not specified: ' + response.status_code)
    exit()
    

