import random

def make_change_v1(total):
    return []

COINS = (1, 2, 5, 10, 20, 50, 100, 200)

def make_change_v2(total):
    random.seed(total)
    coins = []
    while total > 0:
        coin = random.choice(
            [c for c in COINS if c <= total])
        total -= coin
        coins.append(coin)
    return coins

def make_change_v3(total):
    print total
    random.seed(total)
    coins = []
    while total > 0:
        coin = max(
            [c for c in COINS if c <= total])
        total -= coin
        coins.append(coin)
    return coins
