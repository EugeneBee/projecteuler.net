#https://projecteuler.net/problem=54
"""
There is a deliberate logical error in the code. 
Do you understand Python for a long time to find her
"""
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
                one_pair=       1000
                # high_card=         0
                            )
    card_weight = '23456789TJQKA'
    suit_weight = 'SCDH'
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
    #sorted cards
    sorted_cards = sorted(cards, key=card_weight.index)
    #count how many identical cards 
    count_cards = [cards.count(i) for i in cards]

    #checking for cards going in a row 
    #(royal-flach, straight-flush, straight)
    if sorted_cards == list(card_weight[card_weight.index(sorted_cards[0]):
        card_weight.index(sorted_cards[0])+5]):

        #check royal_flush
        if sorted_cards[4] == 'A' and suits.count(suits[0]) == 5:

            full_weight = combin_weight['royal_flush']\
                        + suit_weight.index(suits[0])

        
        #straight-flush
        elif suits.count(suits[0]) == 5:

            full_weight = combin_weight['straight_flush']\
            + card_weight.index(cards[4])*10\
            + suit_weight.index(suits[0])
        #straight
        else:

            full_weight = combin_weight['straight']\
            + card_weight.index(sorted_cards[4])*10\
            + suit_weight.index(suits[cards.index(sorted_cards[4])])
    #check flush
    elif suits.count(suits[0]) == 5:
        full_weight = combin_weight['flush']\
                    + card_weight.index(sorted_cards[4])*10\
                    + suit_weight.index(suits[0])

    #check four
    elif 4 in count_cards:
        full_weight = combin_weight['four']\
                    + card_weight.index(cards[count_cards.index(4)])*10
    #check full house
    elif 3 in count_cards and 2 in count_cards:
        full_weight = combin_weight['full_house']\
                    + card_weight.index(cards[count_cards.index(3)])*10
    #check three
    elif 3 in count_cards:
        full_weight = combin_weight['three']\
                    + card_weight.index(cards[count_cards.index(3)])*10
    #check two pair
    elif 2 in count_cards:
        if count_cards.count(2) == 4:
            full_weight = combin_weight['two_pairs']\
                        + (card_weight.index(sorted_cards[3])\
                        + card_weight.index(sorted_cards[1])/10)*10
    #check one pair
        elif count_cards.count(2) == 2:
            if sorted_cards.index(cards[count_cards.index(2)]) == 3:
                high_card_pair_index = 2
            else:
                high_card_pair_index = 4
            full_weight = combin_weight['one_pair']\
                    + card_weight.index(cards[count_cards.index(2)])*10\
                    + card_weight.index(sorted_cards[high_card_pair_index])/10
                    #only 1 highest card will be checked after a pair to
                    #compare identical pairs
    #high card
    else:
        full_weight = card_weight.index(sorted_cards[0])\
                    + card_weight.index(sorted_cards[1])/10\
                    + card_weight.index(sorted_cards[2])/100\
                    + card_weight.index(sorted_cards[3])/1000
         
    return full_weight

array = []
with open("p054_poker.txt") as file:
    for line in file:
        array.append(line)

result = 0

for item in array:
    tmp_array = item.split()

    if compare_card(tmp_array[:5]) > compare_card(tmp_array[5:]):
        result += 1

print('Result of the problem 54:', result)
