import logging

import requests

logging.basicConfig(filename='pokemon.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')


class PokeAPIWrapper:
    def __init__(self):
        self.base_url = "https://pokeapi.co/api/v2/"
        self.headers = {"Accept": "application/json"}

    def load_pokemon_data(self, pokemon_name):
        URL = self.base_url + f"pokemon/{pokemon_name}"
        try:
            response = requests.get(URL, headers=self.headers)
            response.raise_for_status()
            data = response.json()
            return data
        except requests.exceptions.RequestException as e:
            logging.error(
                f"Error retrieving data for {pokemon_name} at {URL}: {e}")
            return None

    def get_pokemon(self, pokemon_name):
        data = self.load_pokemon_data(pokemon_name)
        if data is not None:
            return {
                "name": data["name"],
                "id": data["id"],
                "type": [type["type"]["name"] for type in data["types"]],
                "abilities": [ability["ability"]["name"]
                              for ability in data["abilities"]],
                "stats": {stat["stat"]["name"]: stat["base_stat"]
                          for stat in data["stats"]},
            }
        else:
            return None

    def get_pokemon_image(self, pokemon_name):
        data = self.load_pokemon_data(pokemon_name)
        if data is not None:
            try:
                return {"image url": data["sprites"]["front_default"]}
            except KeyError:
                logging.error(
                    f"Error retrieving image for {pokemon_name}:\
                     front_default sprite not found.")
                return None

    def get_pokemon_moves(self, pokemon_name):
        data = self.load_pokemon_data(pokemon_name)
        if data is not None:
            moves = []
            for move in data["moves"]:
                moves.append(
                                {
                                    "move": move["move"]["name"],
                                    "url": move["move"]["url"],
                                }
                            )
            return moves

    def search_pokemon_by_type(self, pokemon_type):
        URL = self.base_url + f"type/{pokemon_type}"
        try:
            response = requests.get(URL, headers=self.headers)
            response.raise_for_status()
            pokemon_list = response.json()["pokemon"]
            return [pokemon["pokemon"] for pokemon in pokemon_list]
        except KeyError:
            logging.error(f"Error retrieving pokemon by {pokemon_type}")
            return None
