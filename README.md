

# CorgiDB
<img src="corgidb/CorgiDBlogo.png" alt="CorgiDB logo" style="height:300px; width:300px;" />

Write as short as Corgi's legs but and as fast as a Corgi

CorgiDB is a wrapper of python3's sqlite3 package

<h2>Installation</h2>

```
pip install corgidb
```

<h1>Full Documents</h1>
<h2>CorgiDB Module</h2>

The **CorgiDB** module provides standard accesss to a *.sqlite file and served as the starting point of using corgidb
which can be used to access the **Utils** module of the library

```python
from corgidb import CorgiDB
cdb = CorgiDB(database_path="path/to/db.sqlite")
```

<h2><b>CorgiDB.utils</b> class</h2>

After we construct the **CorgiDB** class the objects provide us with many basic utilities function connect to the previously defined database connection
- create_table(name: str, columns: list)
- delete_table(name: str, keep_table: bool=False)
- get_table(name: str)

<h3>create_table()</h3>

the **create_table** method will create table on the connected database


**Arguments**
  - **name (str)** The name of the table which cannot be duplicate and cannot be named "sqlite_sequence" as the name is being use for auto increment
  - **columns (list)** Table columns name and datatypes in tuple which can be int, float, bool, str

**Return**
- This method will return a **Table** object which will later explained in this document

```python
tb = cdb.utils.create_table(
    name="Personnel",
    columns=[
      (name, str)
      (age, int)
      (mobile, str)
      (height, float)])
```

<h3>delete_table()</h3>

the **delete_table** method will delete named table on the connected database


**Arguments**
  - **name (str)** The Table you wished to delete
  - **keep_table (bool)** delete only data but keep the table default is false

```python
cdb.utils.delete_table(
  name="Personnel"
)
```

<h3>get_table()</h3>

similar to create_table but use with already created table to return Table objects


**Arguments**
- **name (str)** The table you want to create table object

**Return**
- This method will return a **Table** object which will later explained in this document

```python
tb = cdb.utils.get_table(name="Personnel")
```

<h2>Table module</h2>

this is the class mentioned above that generate from **get_table() and create_table()** method


**Methods**
- insert
- update
- remove
- get


This document is incomplete