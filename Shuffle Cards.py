# Program to Shuffle deck of card

import random
import itertools

card = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))

random.shuffle(card)

print("Your cards are:-")
for i in range(13):
     print(card[i][0], "of", card[i][1])
