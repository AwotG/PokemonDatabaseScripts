"""
Main script, will create a new database with requiired tables and views, make the API calls, translate them and then
insert into the database
"""
import contextlib
import pathlib
import sqlite3
import requests

from PokemonTableUtils import Pokemon

if __name__ == '__main__':
    current_dir = pathlib.Path().absolute()
    database_name = "PokemonAPI.db"
    output_database = current_dir / database_name

    db_connection = sqlite3.connect(output_database)
    bulbasaur = requests.get("https://pokeapi.co/api/v2/pokemon/bulbasaur").json()

    with contextlib.closing(sqlite3.connect(output_database)) as db_connection:
        db_connection.row_factory = sqlite3.Row
        pokemon = Pokemon(db_connection)
        pokemon.insert_single_pokemon(bulbasaur)