import pygame as pg
from card import Card
from game import Game 

import config
from deck import Deck
from player import Player

# init game & set title
pg.init()
pg.display.set_caption(config.game["title"])

# set pygame clock
clock = pg.time.Clock()

# font
_font = pg.font.SysFont("Comic Sans MS", 30)

# set size window
_display = pg.display.set_mode(
    config.game["resolution"], config.game["resizable"])

# refresh container
pg.display.flip()

# launch the game
exited = False

cards = []

pos_x = config.card_start_pos_x()
pos_y = config.card_start_pos_y()

print(f"Start X: {pos_x}, Start Y: {pos_y}")

deck = Deck()
deck.generate()
deck.shuffle()

players = [
    Player(name="Romain"),
    Player(name="Ayoub"),
    Player(name="Victor")
]


# Affiche les 4 premières cartes de la party 
party = Game()
party.set_players(players)
party.init_game(players,deck,pos_x,pos_y)



while not exited:
    for e in pg.event.get():
        exited = True if e.type == pg.QUIT else False

    for card in players[0].hand:
        card.draw(_display, _font)
        
    # Affiche la carte suivante dans le deck principal  (à repositionner)
    deck.cards[0].draw(_display, _font)

    pg.display.flip()

    clock.tick(config.game["framerate"])
