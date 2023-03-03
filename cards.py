import random
from datetime import datetime
import json
import os

# load tarot deck
def load():

    # seed random from system time
    random.seed(datetime.now().timestamp())

    cwd = os.getcwd()
    # load card deck
    path = '/'.join((cwd, "static/tarot.json"))
    file = open(path, "r")
    deck = json.load(file)

    return deck

# Draw n cards from the deck
# usually 3 for current version
def draw(n):

    idx = random.sample(range(0,77), n)
    return idx

# generate upright or reverse position based on random
def position():
    if random.random() >= 0.5:
        return "Upright "
    return "Reversed "

