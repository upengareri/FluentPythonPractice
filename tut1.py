import collections
from math import hypot

# NAMED TUPLE
# Two parameters are required to create a named tuple: a class name and a list of
# field names, which can be given as an iterable of strings or as a single space-
# delimited string.

# Card = collections.namedtuple("Card", ["rank", "suit"])  # as an iterable of strings
Card = collections.namedtuple("Card", "rank suit")  # single space delimited string


class FrenchDeck:
    """Example of implementing a sequence like object with inbuilt functions(dunder methods) to
    make the user-defined objects more pythonic
    
    """

    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "clubs diamonds hearts spades".split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


class Vector:
    """Example of implementing a arithmetic object with inbuilt functions(dunder methods) to
    make the user-defined objects more pythonic
    
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __abs__(self):
        return hypot(self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        x = self.x * scalar
        y = self.y * scalar
        return Vector(x, y)

    def __bool__(self):
        return bool(abs(self))


if __name__ == "__main__":
    # -----------Deck -------------
    print(Card("4", "spades"))  # Card(rank='4', suit='spades')
    deck = FrenchDeck()
    print("length of deck: ", len(deck))

    # ---------- Vector -----------
    print("obj repr: ", Vector(2, 3))
    print("addition: ", Vector(2, 4) + Vector(2, 1))
    print("scalar mul: ", Vector(2, 3) * 2)
    print("magnitude: ", abs(Vector(3, 4)))

