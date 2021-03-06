"""
This will be the main table. Will only contain the single value keys, the rest will be connected through association tables.
NOTE: Bulk Insert is much faster, but will fail if any value is invalid.
Using single insert in a for loop is slower but will at least catch the failing entries.
"""
import logging


class Pokemon():
    def __init__(self, sql_connection):
        self.connection = sql_connection
        self.cursor = self.connection.cursor()

    def create_pokemon_table(self):
        insert_msg = """
            CREATE TABLE IF NOT EXISTS "Pokemon" (
                    "pokemon_id"	INTEGER,
                    "pokemon_name"	TEXT,
                    "base_experience"	INTEGER,
                    "height"	INTEGER,
                    "is_default"	TEXT,
                    "location_area_encounters"	TEXT,
                    "order"	INTEGER,
                    "weight"	INTEGER,
                    PRIMARY KEY("pokemon_id")
                );
        """
        self.execute_query(insert_msg)

    def insert_single_pokemon(self, response):
        self.create_pokemon_table()
        columns, values = self.parse_response(response)
        insert_msg = f"""
            INSERT INTO Pokemon {columns}
            values {values}
        """
        self.execute_query(insert_msg)

    def bulk_insert_pokemon(self, response_list):
        #TODO: this will fail if any entry is invalid
        self.create_pokemon_table()
        insert_many = []
        for response in response_list:
            columns, values = self.parse_response(response)
            insert_many.append(str(values))

        insert_msg = f"""
            INSERT INTO Pokemon {columns}
            values {','.join(insert_many)};
        """
        self.execute_query(insert_msg)

    def parse_response(self, response):
        values_dict = dict(pokemon_id=response["id"],
                           pokemon_name=response["name"],
                           base_experience=response["base_experience"],
                           height=response["height"],
                           is_default=response["is_default"],
                           location_area_encounters=response["location_area_encounters"],
                           order=response["order"],
                           weight=response["weight"])
        columns = tuple(key for key in values_dict.keys())
        values = tuple(key for key in values_dict.values())
        return columns, values

    def execute_query(self, msg):
        try:
            self.cursor.execute(msg)
            self.connection.commit()
        except Exception as e:
            logging.error(f"Unable to write to database. Error message:\n{e}")
            self.connection.rollback()
