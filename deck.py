from cards_list import cards_list
from random import shuffle 
from dataclasses import dataclass, field 

@dataclass
class Deck:
    
    cards : list = field(default_factory=list)
    
    def shuffle(self):
        shuffle(self.cards)

    def generate(self):
        self.cards = []
        for i in range( len(cards_list) ):
            self.cards.append(cards_list[i])
    

# deck = Deck()
# deck.generate()
# deck.shuffle()
# print(deck.cards[0:5])
        