# dictionary-api-python-flask/model/dbHandler.py
import sqlite3 as SQL


def match_exact(word: str) -> list:
    """
    This method will:
    1. Accept a string
    2. Search the dictionary for an exact match
    3. If success return the definition
    4. If not return an empty list
    """
    # Establish connection
    db = SQL.connect("data/dictionary.db")
    # Create query
    sql_query = "SELECT * from entries WHERE word=?"
    # Query the database for exact matches
    match = db.execute(sql_query, (word,)).fetchall()
    # Close the connection to the database
    db.close()
    # Return the matches
    return match


def match_like(word: str) -> list:
    """
    This method will:
    1. Accept a string
    2. Search the dictionary for approximate matches
    3. If success return the definition as a list
    4. If not return an empty list
    """
    # Establish connection
    db = SQL.connect("data/dictionary.db")
    # Create query
    sql_query = "SELECT * from entries WHERE word LIKE ?"
    # Query the database for exact matches
    match = db.execute(sql_query, ("%" + word + "%",)).fetchall()
    # Close the connection to the database
    db.close()
    # Return the matches
    return match
