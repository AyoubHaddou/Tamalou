# Actions
# see_self : see one of your card
# see_other : see one of other's cards
# switch: exchange two cards without seeing them

def see_self(hand, card_index):
    card = hand[card_index]
    card.set_visible(True)


def see_other(hand, card_index):
    card = hand[card_index]
    card.set_visible(True)


def switch(player_from, card_index_from, player_to, card_index_to):
    pass
