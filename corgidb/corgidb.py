import sqlite3
from corgidb.objects.table import Table
from corgidb.utils import Utils
class CorgiDB:
    """
    Starting point of using CorgiDB as a sqlite wrapper

    Attributes:
        database_path (str): The path to database file *.sqlite
    """
    def __init__(self, database_path: str):
        self.connection = sqlite3.connect(database_path)
        self.cursor     = self.connection.cursor()

        # Initialize utils class
        self.utils      = Utils(connection=self.connection)

