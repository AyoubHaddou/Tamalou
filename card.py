from pygame import draw, Rect, display
import config
import colors


class Card:

    value: int
    name: str
    owner: int
    pos_x: int
    pos_y: int
    width: int
    height: int
    visible: bool

    def __init__(self, visible):
        self.pos_x = 0
        self.pos_y = 0
        self.visible = visible
        self.width = config.card["width"]
        self.height = config.card["height"]
        self.background = colors.GRAY
        self.value = "9"

    def draw(self, _display, _font) -> None:

        background = colors.WHITE if self.visible else colors.GRAY
        # draw card
        draw.rect(
            _display,
            background,
            Rect(self.pos_x, self.pos_y, self.width, self.height),
            border_radius=config.card["border_radius"]
        )

        if self.visible:
            # display top number
            top_label = _font.render(self.value, 1, colors.BLACK)
            _display.blit(top_label, (self.pos_x + 5, self.pos_y))

            # display bottom number
            bottom_label = _font.render(self.value, 1, colors.BLACK)
            _display.blit(bottom_label, (self.pos_x + 75, self.pos_y + 160))

    def set_coordinates(self, coordinates: tuple) -> None:
        self.pos_x = coordinates[0]
        self.pos_y = coordinates[1]

    def card_total_width(self) -> int:
        return self.width + config.card["padding"]
