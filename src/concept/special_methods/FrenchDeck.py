import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    """
    Although FrenchDeck implicitly inherits from object,4 its functionality is not inherited, but comes from
    leveraging the data model and composition. By implementing the special methods __len__ and __getitem__,
    our FrenchDeck behaves like a standard Python sequence, allowing it to benefit from core language features (e.g.,
    iteration and slicing) and from the standard library, as shown by the examples using random.choice, reversed,
    and sorted. Thanks to composition, the __len__ and __getitem__ implementations can hand off all the work to a
    list object, self._cards.
    """
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


# todo - move test code in Jupyter notebook
deck = FrenchDeck()
print(len(deck))  # 52
print(range(2, 11))  # 2-10
print(deck[0])
print(deck[-1])
print(choice(deck))
print(choice(deck))

print(deck[:3])  # pick top three cards
print(deck[12::13])  # pick just the aces by starting on index 12 and skipping 13 cards at a time

for card in deck:
    print(card)

for card in reversed(deck):
    print(card)

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


for card in sorted(deck, key=spades_high):
    print(card)
