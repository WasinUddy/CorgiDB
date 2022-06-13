---
description: corgidb.package.Table
---

# class Table

Table class is for manipulating SQLite Table which can be generated in 2 ways

1. using CorgiDB.utils `create_table` or `get_table`
2. initialize the class Table manually by calling `corgidb.objects.Table`

However, if the table already exists it is highly recommended to create this object by using the first method

**Parameters**

1.  **name: str**

    name of the Table on the database
2.  **connection: sqlite3.Connection**

    connection to SQLite database using Python's sqlite3 module

**Examples**

```python
import sqlite3
from corgidb.objects import Table

connection = sqlite3.connect("db.sqlite")

tb = Table(name="Personnel", connection=connection)
```

**Notes**

the above method can be automated by using `get_table`

{% content-ref url="../../class-corgidb/corgidb.utils.get_table.md" %}
[corgidb.utils.get\_table.md](../../class-corgidb/corgidb.utils.get\_table.md)
{% endcontent-ref %}

