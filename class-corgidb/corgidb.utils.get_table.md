# CorgiDB.utils.get\_table

```python
CorgiDB.utils.get_table(name: str)
```

this method similar to `CorgiDB.utils.create_table` but instead of creating a new table this method will return `Table` objects of already existed Table

#### **Parameters**

1.  **name : str**

    name of the table, e.g.,  `"Personnel" , "Student"`

**Returns**&#x20;

1.  **out: Table**

    CorgiDB's Table object for us to manipulate the table getting it

{% content-ref url="../table.md" %}
[table.md](../table.md)
{% endcontent-ref %}

**Examples**

```python
from corgidb import CorgiDB

# Connect CorgiDB to db.sqlite
cdb = CorgiDB(database_path="db.sqlite")

# Get the Table
tb = cdb.utils.get_table(
    name="Employee"
)
```

