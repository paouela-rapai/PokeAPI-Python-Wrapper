## PokeAPI Wrapper
PokeAPI Wrapper is a Python module that provides a simple and easy-to-use interface for accessing the [PokéAPI](https://pokeapi.co/) to retrieve data about Pokémon.

## Features
-   Get information about a specific Pokémon by name
-   Get the image of a specific Pokémon by name
-   Get a list of moves of a specific Pokémon by name
-   Search for all Pokémon of a specific type
-   Command-line interface (CLI) using argparse

## Installation
1. Clone this repository:
    ```terminal
    git clone https://github.com/paouela-rapai/PokeAPI-Python-Wrapper.git
	cd <PokeAPI-Python-Wrapper>
    ```	
		
3. Create a virtual environment

    ```terminal
    python -m venv .venv
    ```

4. Activate virtual environment

    ```terminal
    source .venv/bin/activate
    ```

5. Install dependencies

    ```terminal
    pip intall -r requirements.txt    
    ```


## Usage
### Command-line interface

Run the  script `main.py` to access the PokeAPI Wrapper functionalities from the command line:
```
python main.py [-h] [-p POKEMON_NAME] [-i POKEMON_NAME] [-m POKEMON_NAME] [-t POKEMON_TYPE] [-s]

```
    
Arguments:

-   `-h, --help`: show the help message and exit
-   `-p [pokemon], --pokemon [pokemon]`: get information about a specific Pokémon by name
-   `-i [pokemon], --image [pokemon]`: get the image of a specific Pokémon by name
-   `-m [pokemon], --moves [pokemon]`: get a list of moves of a specific Pokémon by name
-   `-t [type], --type [type]`: search for all Pokémon of a specific type

## Acknowledgments

-   [PokéAPI](https://pokeapi.co/) for providing the Pokémon data API