# class CorgiDB

CorgiDB class is the heart of the library that will provide the connection to the database and help user to manipulate the database through its functionality

Initializing a CorgiDB objects and having a \*.sqlite file to work with **must** be the first step of using this library

### What is an \*.sqlite file

An SQLITE file contains a database created with SQLite, a lightweight ([RDBMS](https://techterms.com/definition/rdbms)) widely used in application development for storing embedded databases. SQLITE files are often created by software developers for storing data used by their applications.

{% embed url="https://www.sqlite.org/index.html" %}

### How to create a CorgiDB object ?

Just import it and initailized the class with the path to \*.sqlite file

```python
from corgidb import CorgiDB

cdb = CorgiDB(database_path="path/to/db.sqlite")
```
