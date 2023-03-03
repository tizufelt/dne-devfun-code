import requests
import json
from pprint import pprint



url = "https://pokeapi.co/api/v2/pokemon/"

params = {'limit': 100}

for offset in range(0, 1000, 100):
    params['offset'] = offset  # add new value to dict with `limit`
    response = requests.get(url, params=params)

    if response.status_code != 200: 
        print(response.text)
    else:
        data = response.json()
        #pp.pprint(data)
        for item in data['results']:
            print(item['name'])


    













# #print(jsonResponse)
# response.raise_for_status()
# # access JSOn content
# jsonResponse = response.json()
# print("Entire JSON response")

# # print("Print each key-value pair from JSON response")
# # for key, value in jsonResponse.items():
# #     print(key, ":", value)

# #print(jsonResponse["payload"]['name'])
# #pprint(response.text)

# character = (input("please eneter in a pokemon: "))
# for character in jsonResponse[key, ":" valu]:
#     print(character)

# #pprint(json_data)
