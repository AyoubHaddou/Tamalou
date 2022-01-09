from pygame import display, event, QUIT, init, font
from card import Card

import config

# init game & set title
init()
display.set_caption(config.game["title"])

# font
_font = font.SysFont("Comic Sans MS", 30)

# set size window
_display = display.set_mode(
    config.game["resolution"], config.game["resizable"])

# refresh container
display.flip()

# launch the game
exited = False

cards = []

pos_x = config.card_start_pos_x()
pos_y = config.card_start_pos_y()

print(f"Start X: {pos_x}, Start Y: {pos_y}")

for i in range(4):
    _card = Card(True if i < 2 else False)
    _card.set_coordinates((pos_x, pos_y))

    pos_x += _card.card_total_width()
    cards.append(_card)

while not exited:
    for e in event.get():
        exited = True if e.type == QUIT else False

    for card in cards:
        card.draw(_display, _font)

    display.flip()
