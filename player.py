from card import Card


class Player:
    id: int
    name: str
    hand: list(Card)
    draw: Card

    def __init__(self, name) -> None:
        self.id = str(hash(name))[1:13]
        self.name = name

    def set_hand(self, hand) -> None:
        self.hand = hand

    def switch_card(self, draw_card, target_card) -> None:
        # switch cards in hand property
        # put card in discard
        pass

    def action(self, action_name) -> None:
        # call action
        pass
