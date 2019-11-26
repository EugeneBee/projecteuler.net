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
    combin_weight = dict(
                royal_flush=    9000,
                straight_flush= 8000,
                four=           7000,
                full_house=     6000,
                flush=          5000,
                straight=       4000,
                three=          3000,
                two_pairs=      2000,
                one_pair=       1000,
                high_card=         0
                            )
    card_weight = '23456789TJQKA'
    suit_weight = 'SCHD'
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

    tmp_cards = sorted(cards, key=card_weight.index)
    #check royal_flush
    if tmp_cards == ['T', 'J', 'Q', 'K', 'A'] and suits.count(suits[0]) == 5:

        full_weight = combin_weight['royal_flush']\
                    + suit_weight.index(suits[0])
    # print(sorted(cards, key=card_weight.index))
    
    #checking for cards going in a row (straight and straight-flash)
    elif tmp_cards == card_weight[card_weight.index(tmp_cards[0]):card_weight.index(tmp_cards[0])+6]:

        #straight-flash
        if suits.count(suits[0]) == 5:

            full_weight = combin_weight['straight_flush']\
            + card_weight.index(cards[4])*10\
            + suit_weight.index(suits[0])
        #straight
        else:

            full_weight = combin_weight['straight']\
            + card_weight.index(tmp_cards[4])*10\
            + suit_weight.index(suits[cards.index(tmp_cards[4])])
    #check flush
    elif suits.count(suits[0]) == 5:
        full_weight = combin_weight['flush']\
                    + card_weight.index(tmp_cards[4])*10\
                    + suit_weight.index(suits[0])
    #count how many identical cards 
    count_cards = [cards.count(i) for i in cards]

    #check four
    if 4 in count_cards:
        full_weight = combin_weight['four']\
                    + card_weight.index(cards[count_cards.index(4)])*10

 

    # return full_weight

array = []
with open("p054_poker.txt") as file:
    for line in file:
        array.append(line)

result = 0

for item in array:
    tmp_suit = item.split()

    if compare_card(tmp_suit[:5]) > compare_card(tmp_suit[5:]):
        result += 1



print(tmp_suit)
