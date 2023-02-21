import argparse


def parse_args():
    parser = argparse.ArgumentParser(
        prog="PokeAPI Wrapper",
        description="A command line interface for the PokeAPI.",
        usage=""
    )
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version="%(prog)s 1.0",
    )
    parser.add_argument(
        "--get_pokemon",
        help="Get information about a specific Pokemon",
        type=str,
    )
    parser.add_argument(
        "-i",
        "--image",
        help="Get the image URL for a specific Pokemon",
        type=str,
    )
    parser.add_argument(
        "-m",
        "--moves",
        help="Get a list of moves that a specific Pokemon can learn",
        type=str,
    )
    parser.add_argument(
        "-t",
        "--type",
        help="Search for Pokemon of a specific type",
        type=str,
    )
    return parser.parse_args()
