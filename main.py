from fastapi import FastAPI
from typing import Optional
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
def dictionary(word: str):
    """
    DEFAULT ROUTE
    This method will
    1. Accept a word from the request
    2. Try to find an exact match, and return it if found
    3. If not found, find all approximate matches and return
    """
    if not word:
        response = {'status': 'error', 'word': word, 'data': 'word not found'}
        return response

    definitions = match_exact(word)
    if definitions:
        response = {'status': 'success', 'word': word, 'data': definitions}
        return response

    definitions = match_like(word)
    if definitions:
        response = {'status': 'success', 'word': word, 'data': definitions}
        return response
    else:
        response = {'status': 'error', 'word': word, 'data': 'word not found'}
        return response
