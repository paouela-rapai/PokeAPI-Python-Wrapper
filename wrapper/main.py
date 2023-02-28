from utils.loader import parse_args
from utils.pokeapi_wrapper import PokeAPIWrapper

if __name__ == '__main__':
    args = parse_args()

    wrapper = PokeAPIWrapper()

    if args.pokemon:
        print(wrapper.get_pokemon(args.pokemon))
    elif args.image:
        print(wrapper.get_pokemon_image(args.image))
    elif args.moves:
        print(wrapper.get_pokemon_moves(args.moves))
    elif args.type:
        print(wrapper.search_pokemon_by_type(args.type))
