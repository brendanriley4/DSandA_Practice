-SQL is case insensitive, formal folks like all caps

Select one row of data:
```SQL
query = """
select * from Projects limit 1;
"""
```

To select specific rows:
```SQL
query = """
select id, name, deadline, completed, department_id from Projects limit 5;
"""
```

To order the output specifically can use:
```SQL
query = """
select * from Projects order by Name desc;
"""
```

To sort in multiple orders (sorts first by deadline in ascending order, then by name in descending order):
```SQL
query = """
select * from Projects order by deadline asc, name desc;
"""
```


