from pygame import init
from card import Card
from dataclasses import dataclass, field


@dataclass
class Player:
    name: str = field(default_factory=str, init=True)
    id: int = str(hash(name))[1:13]
    hand: list = field(default_factory=list)

    def append_hand(self, card) -> None:
        self.hand.append(card)

    def switch_card(self, source_card, target_card) -> None:
        # switch cards in hand property
        # put card in discard
        pass

    def action(self, action_name) -> None:
        # call action
        pass
