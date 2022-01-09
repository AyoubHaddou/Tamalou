# actions
# see_self : see one of your card
# see_other : see one of other's cards
# switch: exchange two cards without seeing them


cards_list = [
    {
        "name": "1",
        "value": 1,
        "color" : "black",
        "actions": [],
        "ID" : 1
    },
    {
        "name": "1",
        "value": 1,
        "color" : "black",
        "actions": [],
        "ID" : 2
    },
    {
        "name": "1",
        "value": 1,
        "color" : "red",
        "actions": [],
        "ID" : 3
    },
    {
        "name": "1",
        "value": 1,
        "color" : "red",
        "actions": [],
        "ID" : 4
    },
    {
        "name": "2",
        "value": 2,
        "color" : "black",
        "actions": [],
        "ID" : 5
    },
    {
        "name": "2",
        "value": 2,
        "color" : "black",
        "actions": [],
        "ID" : 6
    },
    {
        "name": "2",
        "value": 2,
        "color" : "red",
        "actions": [],
        "ID" : 7
    },
    {
        "name": "2",
        "value": 2,
        "color" : "red",
        "actions": [],
        "ID" : 8
    },
    {
        "name": "3",
        "value": 3,
        "color" : "black",
        "actions": [],
        "ID" : 9
    },
    {
        "name": "3",
        "value": 3,
        "color" : "black",
        "actions": [],
        "ID" : 10
    },
    {
        "name": "3",
        "value": 3,
        "color" : "red",
        "actions": [],
        "ID" : 11
    },
    {
        "name": "3",
        "value": 3,
        "color" : "red",
        "actions": [],
        "ID" : 12
    },
    {
        "name": "4",
        "value": 4,
        "color" : "black",
        "actions": [],
        "ID" : 13
    },
    {
        "name": "4",
        "value": 4,
        "color" : "black",
        "actions": [],
        "ID" : 14
    },
    {
        "name": "4",
        "value": 4,
        "color" : "red",
        "actions": [],
        "ID" : 15
    },
    {
        "name": "4",
        "value": 4,
        "color" : "red",
        "actions": [],
        "ID" : 16
    },
    {
        "name": "5",
        "value": 5,
        "color" : "black",
        "actions": [],
        "ID" : 17
    },
    {
        "name": "5",
        "value": 5,
        "color" : "black",
        "actions": [],
        "ID" : 18
    },
    {
        "name": "5",
        "value": 5,
        "color" : "red",
        "actions": [],
        "ID" : 19
    },
    {
        "name": "5",
        "value": 5,
        "color" : "red",
        "actions": [],
        "ID" : 20
    },
     {
        "name": "6",
        "value": 6,
        "color" : "black",
        "actions": [],
        "ID" : 21
    },
    {
        "name": "6",
        "value": 6,
        "color" : "black",
        "actions": [],
        "ID" : 22
    },
    {
        "name": "6",
        "value": 6,
        "color" : "red",
        "actions": [],
        "ID" : 23
    },
    {
        "name": "6",
        "value": 6,
        "color" : "red",
        "actions": [],
        "ID" : 24
    },
    {
        "name": "7",
        "value": 7,
        "color" : "black",
        "actions": [],
        "ID" : 25
    },
    {
        "name": "7",
        "value": 7,
        "color" : "black",
        "actions": [],
        "ID" : 26
    },
    {
        "name": "7",
        "value": 7,
        "color" : "red",
        "actions": [],
        "ID" : 27
    },
    {
        "name": "7",
        "value": 7,
        "color" : "red",
        "actions": [],
        "ID" : 28
    },
    {
        "name": "8",
        "value": 8,
        "color" : "black",
        "actions": [],
        "ID" : 29
    },
    {
        "name": "8",
        "value": 8,
        "color" : "black",
        "actions": [],
        "ID" : 30
    },
    {
        "name": "8",
        "value": 8,
        "color" : "red",
        "actions": [],
        "ID" : 31
    },
    {
        "name": "8",
        "value": 8,
        "color" : "red",
        "actions": [],
        "ID" : 32
    },
    {
        "name": "9",
        "value": 9,
        "color" : "black",
        "actions": ["see_self"],
        "ID" : 33
    },
    {
        "name": "9",
        "value": 9,
        "color" : "black",
        "actions": ["see_self"],
        "ID" : 34
    },
    {
        "name": "9",
        "value": 9,
        "color" : "red",
        "actions": ["see_self"],
        "ID" : 35
    },
    {
        "name": "9",
        "value": 9,
        "color" : "red",
        "actions": ["see_self"],
        "ID" : 36
    },
    {
        "name": "10",
        "value": 9,
        "color" : "black",
        "actions": ["see_other"],
        "ID" : 37
    },
    {
        "name": "10",
        "value": 9,
        "color" : "black",
        "actions": ["see_other"],
        "ID" : 38
    },
    {
        "name": "10",
        "value": 9,
        "color" : "red",
        "actions": ["see_other"],
        "ID" : 39
    },
    {
        "name": "10",
        "value": 9,
        "color" : "red",
        "actions": ["see_other"],
        "ID" : 40
    },
    {
        "name": "V",
        "value": 10,
        "color" : "black",
        "actions": ["switch"],
        "ID" : 41
    },
    {
        "name": "V",
        "value": 10,
        "color" : "black",
        "actions": ["switch"],
        "ID" : 42
    },
    {
        "name": "V",
        "value": 10,
        "color" : "red",
        "actions": ["switch"],
        "ID" : 43
    },
    {
        "name": "V",
        "value": 10,
        "color" : "red",
        "actions": ["switch"],
        "ID" : 44
    },
    {
        "name": "D",
        "value": 10,
        "color" : "black",
        "actions": [],
        "ID" : 45
    },
    {
        "name": "D",
        "value": 10,
        "color" : "black",
        "actions": [],
        "ID" : 46
    },
    {
        "name": "D",
        "value": 10,
        "color" : "red",
        "actions": [],
        "ID" : 47
    },
    {
        "name": "D",
        "value": 10,
        "color" : "red",
        "actions": [],
        "ID" : 48
    },
    {
        "name": "R",
        "value": 15,
        "color" : "black",
        "actions": ["switch"],
        "ID" : 49
    },
    {
        "name": "R",
        "value": 15,
        "color" : "black",
        "actions": [],
        "ID" : 50
    },
    {
        "name": "R",
        "value": 0,
        "color" : "red",
        "actions": [],
        "ID" : 51
    },
    {
        "name": "R",
        "value": 0,
        "color" : "red",
        "actions": [],
        "ID" : 52
    },
    {
        "name": "J",
        "value": -1,
        "color" : "red",
        "actions": [],
        "ID" : 53
    },
    {
        "name": "J",
        "value": -1,
        "color" : "red",
        "actions": [],
        "ID" : 53
    },
]
