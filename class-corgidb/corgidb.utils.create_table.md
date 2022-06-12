# CorgiDB.utils.create\_table



```python
CorgiDB.utils.create_table(name: str, columns: list)
```

this method will create\_table on the connected database

#### **Parameters**&#x20;

1.  **name : str**

    name of the table, e.g., `"Personnel"`, `"Student"`
2.  **columns : list**

    columns contain in the table in form of `("Columns name", dtype)` in list

    e.g., `[("name", str), ("age", int)]` with only `int, float, bool, str` are supported

**Returns**

1.  out : Table

    CorgiDB's Table object for us to manipulate the table after the creation

{% content-ref url="../table.md" %}
[table.md](../table.md)
{% endcontent-ref %}

#### Notes

Creating an already existing Table will raise an SQLite3 error

#### Examples

```python
from corgidb import CorgiDB

# Connect CorgiDB to db.sqlite
cdb = CorgiDB(database_path="db.sqlite")

# Create a Table
tb = cdb.utils.create_table(
    name="Employee"
    columns=[
        ("name"     , str),
        ("gender"   , str),
        ("age"      , int),
        ("height"   , float),
        ("weight"   , float)
])
```







****

****

****
