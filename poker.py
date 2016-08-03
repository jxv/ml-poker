import itertools
import copy
import random

def concat(xs):
    return list(itertools.chain.from_iterable(xs))

suits = ['c','s','h','d']
ranks = [1,2,3,4,5,6,7,8,9,10,11,12,13] # ['a','2','3','4','5','6','7','8','9','10','j','q','k']
deck = concat([[(suit, rank) for rank in ranks] for suit in suits])

def generate_deal(player_count):
    shuffled_deck = copy.deepcopy(deck)
    random.shuffle(shuffled_deck)
    table = shuffled_deck[:5]
    players = []
    for i in range(player_count):
        offset = i * 2
        players.append(shuffled_deck[(5 + offset):(7 + offset)])
    return { 'table': table, 'players': players }

def generate_set(player_count, deals):
    return [ generate_deal(player_count) for i in range(deals) ]


