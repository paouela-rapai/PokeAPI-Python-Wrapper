from utils.loader import parse_args
from utils.pokeapi_wrapper import PokeAPIWrapper

if __name__ == '__main__':
    args = parse_args()

    pokemon = PokeAPIWrapper()

    if args.get_pokemon:
        print(pokemon.get_pokemon(args.get_pokemon))
    elif args.image:
        print(pokemon.get_pokemon_image(args.image))
    elif args.moves:
        print(pokemon.get_pokemon_moves(args.moves))
    elif args.type:
        print(pokemon.search_pokemon_by_type(args.type))
