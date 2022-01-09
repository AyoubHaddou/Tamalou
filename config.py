import pygame
import colors

game = {
    "title": "Tamalou",
    "resolution": (1280, 720),
    "resizable": False  # pygame.RESIZABLE
}

card = {
    "width": 100,
    "height": 200,
    "padding": 30,
    "border_radius": 6,
    "background": colors.GRAY,
}

# get total card width including padding


def card_start_pos_x() -> int:
    return (game["resolution"][0] / 2) - \
        ((4*(card["width"] + card["padding"])) / 2)


def card_start_pos_y() -> int:
    return (game["resolution"][1] / 2) + (card["height"] / 2)
