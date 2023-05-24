import random
from Card import Card
from constants import suits, ranks


class Deck:
    def __init__(self):
        self.deck = []

    def get_shuffled_deck(self):
        for suit in suits:
            for rank in ranks:
                card = Card(suit, rank)
                self.deck.append(card)

        random.shuffle(self.deck)

        return self.deck
