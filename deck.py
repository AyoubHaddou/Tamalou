from cards_list import cards_list
from random import shuffle
from card import Card
from dataclasses import dataclass, field


@dataclass
class Deck:

    cards: list = field(default_factory=list)
    discard: list = field(default_factory=list)

    def shuffle(self) -> None:
        shuffle(self.cards)

    def generate(self) -> None:
        index = 0
        for card in cards_list:
            for _ in range(card["instances"]):
                index += 1
                # generates one card per instance of card
                self.cards.append(Card(
                    id=index,
                    name=card["name"],
                    value=card["value"],
                    color=card["color"],
                    visible=True
                ))

        print(f"{len(self.cards)} generated!")

# deck = Deck()
# deck.generate()
# deck.shuffle()
# print(deck.cards[0:5])
