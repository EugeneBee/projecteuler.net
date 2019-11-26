import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:

    ranks = [str(n) for n in range(2, 10)] + list('TJQKA')
    suits = 'C H S D'.split() #spades diamonds club hearts

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                       for rank in self.ranks]
    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

suit_values = dict(C=3, H=2, S=1, D=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

def compare_card(card_array):
    card_str = '23456789TJQKA'
    suit_str = 'SCHD'
    cards = [
                card_array[0][0],
                card_array[1][0],
                card_array[2][0],
                card_array[3][0],
                card_array[4][0]
            ]

    suits = [
                card_array[0][1],
                card_array[1][1],
                card_array[2][1],
                card_array[3][1],
                card_array[4][1]
            ]
    if sorted(cards) == ['A', 'J', 'K', 'Q', 'T']


file = open("p054_poker.txt")
array = file.read().split('\n')
array.remove('')
result = 0

for item in array:
    tmp_suit = item.split()

    if compare_card(tmp_suit[:5]) > compare_card(tmp_suit[5:]):
        result += 1



    print()
