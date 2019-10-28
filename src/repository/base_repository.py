import sqlite3
from ..meta.singleton import Singleton

def get_connection():
    return sqlite3.connect('foo.db')

class BaseReopository(metaclass=Singleton):
    def __init__(self):
        pass