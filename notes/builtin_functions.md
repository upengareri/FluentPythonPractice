### Built-in and Higher order functions

> (For a simple case) A higher order function is a function that takes another function as its argument.

1. `enumerate(iterable, start=0)`
- is used to record index of an iterator
__Most used case:__
```
with open('data.txt', 'r') as f:
    for i, line in enumerate(f, start=1):
        print(f"Line number: {i}")

2. Sorting
    1. `list.sort(key=None, reverse=False)`
    > It modifies the list `in-place`
    > Used only with list
    ```
    a = [4, 3, 5, 1, 2]
    a.sort(reverse=True) >> [5, 4, 3, 2, 1]
    ```

    2. `sorted(iterable, key=None, reverse=False)`
    > Returns a new sorted list from the iterable
    > Used with any iterable



