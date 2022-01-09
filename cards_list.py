# actions
# see_self : see one of your card
# see_other : see one of other's cards
# switch: exchange two cards without seeing them


cards_list = [
    {
        "name": "1",
        "value": 1,
        "actions": [],
        "instances": 4
    },
    {
        "name": "2",
        "value": 2,
        "actions": [],
        "instances": 4
    },
    {
        "name": "3",
        "value": 3,
        "actions": [],
        "instances": 4
    },
    {
        "name": "4",
        "value": 4,
        "actions": [],
        "instances": 4
    },
    {
        "name": "5",
        "value": 5,
        "actions": [],
        "instances": 4
    },
    {
        "name": "6",
        "value": 6,
        "actions": [],
        "instances": 4
    },
    {
        "name": "7",
        "value": 7,
        "actions": [],
        "instances": 4
    },
    {
        "name": "8",
        "value": 8,
        "actions": [],
        "instances": 4
    },
    {
        "name": "9",
        "value": 9,
        "actions": ["see_self"],
        "instances": 4
    },
    {
        "name": "10",
        "value": 10,
        "actions": ["see_other"],
        "instances": 4
    },
    {
        "name": "V",
        "value": 10,
        "actions": ["switch"],
        "instances": 4
    },
    {
        "name": "D",
        "value": 10,
        "actions": [],
        "instances": 4
    },
    {
        "name": "R",
        "value": 15,
        "actions": ["switch", "see_self"],
        "instances": 4
    },
    {
        "name": "R",
        "value": 15,
        "actions": [],
        "instances": 4
    },
    {
        "name": "J",
        "value": -1,
        "actions": [],
        "instances": 2
    },
]
