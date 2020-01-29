### DATA STRUCTURES:
1. __tuple__ (packing and unpacking)
2. __dictionary__ (6 types)
   > 1. __`__get__` (d[k])__
   > 2. __`d.get(k)` - when reading__
   > 3. __d.setdefault(k, []) and d = defaultdict(list)__
   > 4. __collections.OrderedDict() - keeping keys in insertion order__
   > 5. __collections.Counter([iterable-or-mapping])__
   > 6. __from types import MappingProxyType - to not add any extra key but only read and update__
3. __set and frozenset__ : similar to list but unique items and set theory support
    1. set theory - or, and, sub(subtract), xor, subset, proper subset
        superset, proper superset, in(`__contains__`))
    2. additional methods -
        1. to add - s.add(e)
        2. to remove 
            1. s.clear(): remove all elements
            2. s.pop(): removes and returns e else KeyError if empty set
            3. s.discard(e): remove e from s if it is present
            4. s.remove(e): like II but KeyError if not present
        3. len(s)
4. __array__ (to store only numbers): import array.array 
5. __list__ - when nothing fits in 1 to 4 ;)

            