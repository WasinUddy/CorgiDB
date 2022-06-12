---
description: >-
  This page gives a brief introduction to the library. It assumes you have the
  library installed, if you don't check the installation portion
---

# Quickstart

### Simple database

Let's make a simple database first by creating a database file such as **db.sqlite** then we will let CorgiDB connect to the database\


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

# Let's add some data to the table
tb.insert(data={
    "name"    : "Atinat Pramoj",
    "gender"  : "male",
    "age"     : 50,
    "height"  : 170,
    "weight"  : 85
})
```

Now if we check the **db.sqlite** file there will be a table name "Employee" created with "Atinat Pramoj" data in it from now on will deep dive into every function of CorgiDB
