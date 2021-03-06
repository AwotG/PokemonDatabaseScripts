# Pokemon API Database Filling Scripts

These scripts are meant to take the [Pokemon API](https://pokeapi.co/) calls, transform them into a 
relational format, create a database for them and to provide functions to reconstruct into 
the same API response.

This is meant for practice translating a somewhat complicated JSON format into a relational 
database, and to transform it back. 

There are many other uses for this such as:

1. A caching system, so that if you were worried about API rate limiting, can save all information locally 
   and provide to others
   
2. More freedom to use the data in interesting ways (maybe comparing pokemon stats easily)

First round will be using pure SQL calls, wrapped around Pythons built-in SQLite library
There are Python libraries that abstract the SQL side of things, however learning 
the pure SQL implementation is good practice and gives options in the future when
deciding which tools to use. 


