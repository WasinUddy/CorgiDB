import sqlite3

from corgidb.constants import *
from corgidb.exceptions import *

class Table:
    """
    This is a class for manipulating SQL table can be generated from utils.create_table or utils.get_table method
    
    Attributes:
        name (str)  : The name of table
        connection (sqlite3.Connection) : Connection to Database

    """

    def __init__(self, name: str, connection: sqlite3.Connection):
        """
        The constructor for Table class

        Parameters:
            name (str)  : The name of table
            connection (sqlite3.Connection) : Connection to Database
        """
        self.name       = name
        self.connection = connection
        self.cursor     = self.connection.cursor()
    

    def insert(self, data: dict):
        """
        This function insert new data to table function will convert dtype if possible

        Parameters:
            data (dict) : inserted data {col_name: data} 
        """
        cols       = self.cols()
        table_cols = set(cols.keys())
        
        # DataKey mismatch
        if set(data.keys())!=table_cols:
            raise InsertdatakeyMismatchError(set(data.keys), table_cols)

        table_cols = tuple(table_cols)
        insert_data = tuple([cols[col](data[col]) for col in table_cols])

        self.__sqlcmd(f"INSERT INTO {self.name} {table_cols} VALUES {insert_data};")
    
    
    def cols(self, dtype: str='Python', withid: bool=False) -> dict:
        """
        This function get the informations of Table Columns

        Parameters:
            dtype   (str) : setting for which dtype to be output Python(type default) or SQL(string)
            withid  (bool): Including row_id
        Returns:
            dict    : dictionary of columns {colname: dtypes} dtypes as python's type
        """
        dtype_inv = {v: k for k, v in SQLDATATYPE.items()}
        out = {}
        columns = self.__sqlcmd(f"PRAGMA table_info({self.name})").fetchall()

        if withid:
            for column in columns:
                if dtype.upper()=="SQL":
                    out[column[1]] = column[2]
                    continue
                if dtype.upper()=="PYTHON":
                    out[column[1]] = dtype_inv[column[2].upper()]
        else:
            for column in columns[1:]:
                if dtype.upper()=="SQL":
                    out[column[1]] = column[2]
                    continue
                if dtype.upper()=="PYTHON":
                    out[column[1]] = dtype_inv[column[2].upper()]
        return out

    def delete(self, keep_table:bool=False):
        """
        Delete table on database

        Parameters
            name        (str)   : Name of the Table that you wish to be delete
            keep_table  (bool)  : Delete only data of the table if this is False the object will be deleted as well
        """
        if keep_table:
            self.sqlcmd(f"TRUNCATE TABLE {self.name};")
        else:
            self.sqlcmd(f"DROP TABLE {self.name};")



    def __sqlcmd(self, command: str, raw=True):
        """
        This function to execute raw SQL command not recommened to be called if not necessary cannot return any data

        Parameters:
            command (str)   : Raw SQLite command
        
        Returns:
            list            : a list of fetched sql data return empty list if not fetched
        """
        if not raw:
            with self.connection:
                if "SELECT" in command.upper(): 
                    self.cursor.execute(command)
                    return self.cursor.fetchall()
                else:
                    self.cursor.execute(command)
                    return []
        else:
            with self.connection:
                return self.cursor.execute(command)


