# corgidb.objects.Table.cols

```python
Table.cols(dtype: str="Python", withid: bool=False)
```

this method will return table columns and dtype of each column

**Parameters**

1.  **dtype: str**

    choose default output for data type can be selected either `"Python"` or `"SQL"`

    if selected python dtype out will be a type object and string for SQL., e.g. `"LONGTEXT"`
2.  **withid: bool**

    to include `row_id` columns or not

**Returns**

1.  **out: dict**

    dictionary with columns name as key and datatype as value, e.g.`{"name": str}`, `{"name":"LONGTEXT"}`

**Examples**

```python
from corgidb import CorgiDB

cdb = CorgiDB(database_path="db.sqlite")

tb = cdb.get_table(name="Personnel")

tb.cols()

## OUT
{
    "name": str,
    "age" : int
}

```

