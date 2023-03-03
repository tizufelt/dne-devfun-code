import requests


url = "https://deckofcardsapi.com/api/deck/new/"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

