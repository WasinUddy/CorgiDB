# CorgiDB.utils.delete\_table

```python
CorgiDB.utils.delete_table(name: str, keep_table: bool=False)
```

as the name stated this method will delete the table

**Parameters**

1.  **name : str**

    name of the table, e.g., `"Personnel" , "Students"`
2.  **keep\_table : bool**

    keep the table or not if set as `True` only the data will be deleted

**Examples**

```python
from corgidb import CorgiDB

# Connect CorgiDB to db.sqlite
cdb = CorgiDB(database_path="db.sqlite")

# Delete a Table
tb = cdb.utils.delete_table(name="Employee")
```
