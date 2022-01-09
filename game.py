from cards_list import cards_list
from random import shuffle
from card import Card
from dataclasses import dataclass, field

@dataclass
class Game:
    players : list = field(default_factory=list)
    
    
    def set_players(self,players):
        self.players = players
    
    
    def init_game(self,players, deck ,pos_x,pos_y,):
        for i in range(4):
            for player in players:
                card = deck.cards.pop(0)
                card.set_coordinates((pos_x, pos_y))
                player.append_hand(card)
            pos_x += card.total_width()
        
        