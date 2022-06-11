# CorgiDB
Write as short as Corgi's legs but and as fast as a Corgi

CorgiDB is a wrapper of python3's sqlite3 package

<h2>Installation</h2>

```
pip install corgidb
```

<h2>Usage</h2>
Initialize corgidb object by giving the package the path to *.sqlite file

```python
from corgidb import CorgiDB
cdb = CorgiDB(database_path="path/to/db.sqlite")
```

Example corgidb style

```python
table_0 = cdb.utils.create_table(name="table_0", columns=[
  ("name", str),
  ("age", int),
  ("human", bool)
])

# insert new data
table_0.insert(data={
  "name": "Theodore",
  "age":50,
  "women":0
})

# Queried
from corgidb.objects import Condition

condition = Condition(conditions=["human = 1", "age >= 50"], logic='OR')
queried = table_0.get(condition=condition)
queried.saveas_csv("data.csv")


