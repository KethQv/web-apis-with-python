from fastapi import FastAPI, Query
from typing import Optional, List
from model.dbHandler import match_exact, match_like

app = FastAPI()


@app.get("/")
def index():
    """
    DEFAULT ROUTE
    This method will
    1. Provide usage instructions formatted as JSON
    """
    response = {'usage': '/dict?word=<word>'}
    return response


@app.get("/dict")
def dictionary(words: List[str] = Query(None)):
    """
    DEFAULT ROUTE
    This method will
    1. Accept a word from the request
    2. Try to find an exact match, and return it if found
    3. If not found, find all approximate matches and return
    """
    if not words:
        response = {'status': 'error', 'words': words, 'data': 'word not found'}
        return response

    # Initialize response
    response = {'words': []}

    for word in words:
        definitions = match_exact(word)
        if definitions:
            response['words'].append({'status': 'success', 'word': word, 'data': definitions, 'data-type': 'exact'})
        else:
            definitions = match_like(word)
            if definitions:
                response['words'].append({'status': 'success', 'word': word, 'data': definitions, 'data-type': 'approximate'})
            else:
                response['words'].append({'status': 'error', 'word': word, 'data': 'word not found'})
    return response
