# class Condition

This a class for creating an SQLite Condition to use with other CorgiDB methods

```python
corgidb.objects.Condition(conditions: list, logic:str)
```

**Parameters**

1.  **conditions: list**

    list of conditions use None if you don't want any condition, e.g. `["name=Robert", "age>=50"]`
2.  **logic: str**

    logic between conditions can be `"AND" "OR"`

Examples

```python
from corgidb.object import Condition

c = Condition(conditions=[
    "age >= 30"
    "gender = male"
], logic="AND")
```
