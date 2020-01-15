# Example run: python word_occurence.py README.md

import sys
import re

WORD_RE = re.compile(r'\w+')

def inefficient_way_of_counting_words():
    index = {}
    with open(sys.argv[1]) as f:
        for line_num, line in enumerate(f, 1):  # enumerate returns line num first
            for match in WORD_RE.finditer(line):
                word = match.group()
                column_num = match.start() + 1
                location = (line_num, column_num)
                # inefficient way of updating a dictionary if the key is unknown
                occurrences = index.get(word, [])
                occurrences.append(location)
                index[word] = occurrences
    return index

def efficient_way_of_counting_words_using_setdefault():
    index = {}
    with open(sys.argv[1]) as f:
        for line_num, line in enumerate(f, 1):
            for match in WORD_RE.finditer(line):
                word = match.group()
                column_num = match.start() + 1
                location = (line_num, column_num)
                # efficient way of updating dictionary if key is unknown
                # this will use one look-up in hash table to update the value
                index.setdefault(word, []).append(location)
        return index

def efficient_way_of_counting_words_using_defaultdict():
    import collections
    index = collections.defaultdict(list)
    with open(sys.argv[1]) as f:
        for line_num, line in enumerate(f, 1):
            for match in WORD_RE.finditer(line):
                word = match.group()
                column_num = match.start() + 1
                location = (line_num, column_num)
                index[word].append(location)
    return index

ineff_index = inefficient_way_of_counting_words()
eff_index_1 = efficient_way_of_counting_words_using_setdefault()
eff_index_2 = efficient_way_of_counting_words_using_defaultdict()

""" ************** NOTE *********************
the end result of this line
    my_dict.setdefault(key, []).append(new_value)
is same as
    if key not in my_dict:
        my_dict[key] = []
    my_dict[key].append(new_value)
EXCEPT THAT THE LATTER CODE PERFORMS AT LEAST TWO SEARCHES - THREE IF NOT'S FOUND
- WHILE SETDEFAULT DOES IT ALL IN ONE LOOKUP
"""

print("---------- INEFFICIENT start-------")
for word in sorted(ineff_index, key=str.lower):
    print(word, ineff_index[word])

print("---------- INEFFICIENT end-------")
print('\n')
print("---------- EFFICIENT(SETDEFAULT) start-------")
for word in sorted(eff_index_1, key=str.lower):
    print(word, eff_index_1[word])
print("---------- EFFICIENT(SETDEFAULT) end-------")
print('\n')
print("---------- EFFICIENT(DEFAULTDICT) start-------")
for word in sorted(eff_index_2, key=str.lower):
    print(word, eff_index_2[word])
print("---------- EFFICIENT(DEFAULTDICT) end-------")

"""
LESSONS LEARNED:
    1. use get() if we just want to read key which may or may not be present in dict
    2. use setdefault() if we need to update the key which may not exist
    3. defaultdict() is another alternative of setdefault when dealing with modifying
        dictionary whose key may be missing
    4. use of finditer() - it gives the matched regex and also provides us with
       its POSITION i.e. start and end column number of the matched word
       example:
        >>> text = "He was carefully disguised but captured quickly by police."
        >>> for m in re.finditer(r"\w+ly", text):
        ...     print('%02d-%02d: %s' % (m.start(), m.end(), m.group(0)))
                07-16: carefully
                40-47: quickly
"""

"""
A BRIEF OVERVIEW OF DICTIONARY
1. __getitem__ or the most basic way d[k]
2. get() for read-only mode of searching key(and its value) which may be missing in dict
3. setdefault() and collections.defaultdict() for updating keys which may be missing in dict
4. collections.OrderedDict() for maintaining keys in insertion order
5. collections.Counter() a mapping that holds integer count for each key. It can be used for
    example in finding how many occurences of letter say 'u' in my name
6. from types import MappingProxyType
    immutable mapping/dictionary so that the user can only update the values of the keys and
    not add any extra key or modify a key. Example in GPIO pins (e.g rasberry Pi board),
    the pins of the board couls be used as immutable dict where the user can only change the
    pins value but not the pin itself which is mapped to the dictionary through key
"""
