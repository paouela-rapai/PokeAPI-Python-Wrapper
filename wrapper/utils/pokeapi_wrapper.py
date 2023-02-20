import requests

url = "https://pokeapi.co/api/v2/pokemon/1"
headers = {
    "Accept": "application/json"
}
response = requests.get(url, headers=headers)
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Error: could not retrieve data")


class PokeAPIWrapper:
    pass
