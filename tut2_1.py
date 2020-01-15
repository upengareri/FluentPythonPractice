# TOPICS: SEQUENCE: tuple unpacking, slicing, sorting and searching
### TUPLE UNPACKING / PARALLEL ASSIGNMENT

# 1 Simple unpacking
import os

_, filename = os.path.split("/home/abc/.ssh/idrsa.pub")
print(f"filename: {filename}")  # idrsa.pub


# 2 Using * to grab excess items (Star unpacking - my version)
a, b, *rest = range(5)  # 0, 1, [2, 3, 4]
a, b, *rest = range(2)  # 0, 1, []
*rest, a, b = range(5)  # [0, 1, 2], 3, 4
a, *rest, b = range(5)  # 0, [1, 2, 3], 4


# 3 Prefixing argument
def divmod(x, y):
    quotient = x / y
    remainder = x % y
    return quotient, remainder


q, r = divmod(20, 8)  # (2, 4)
t = (20, 8)
q, r = divmod(*t)  # (2, 4)  PREFIXING ARGUMENT


##################################################

### SORTING and SEARCHING(/INSERTING) built-in functions

# .sort() [IN PLACE SORTING], sorted() [CREATES A NEW COPY]
marks = [40, 20, 9, 23, 90, 87]  # returns a new object with sorted items
sorted(marks)  # [9, 20, 23, 40, 87, 90]
marks.sort()  # in-place sorting so returns None (all in-place method returns None to let users now)

# bisect module has in-built binary search algorithm
# two main functions within bisect
# bisect.bisect(), bisect.insort()

import bisect

# APPLICATION: Convert marks of students into grades
def grade(score, breakpoints=[60, 70, 80, 90], grades="FDCBA"):
    position = bisect.bisect(score, breakpoints)
    return grades[position]


student_grades = [grade(score) for score in marks]

#########################################################
# list and tuple are sequences but set is not a sequence
# set is just a container whose contents are unordered

## DOING A LOT OF MEMBERSHIP CHECKING?
## example: if item in my_collection
## then use set instead of list (it's FAST)

# double means double precision float
# storing millions of numbers in an object is best achieved by array.array or pickle dump
#
