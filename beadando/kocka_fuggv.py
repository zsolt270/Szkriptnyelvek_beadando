import random


def dobas(size):
    eredmeny = 0
    dice100 = [00, 10, 20, 30, 40, 50, 60, 70, 80, 90]
    if size == 6:
        dice1 = random.randint(1, 6)
        eredmeny = "Dobott eredmény: {}".format(dice1)
    elif size == 4:
        dice1 = random.randint(1, 4)
        eredmeny = "Dobott eredmény: {}".format(dice1)
    elif size ==8:
        dice1 = random.randint(1, 8)
        eredmeny = "Dobott eredmény: {}".format(dice1)
    elif size == 10:
        dice1 = random.randint(1, 10)
        eredmeny = "Dobott eredmény: {}".format(dice1)
    elif size == 12:
        dice1 = random.randint(1, 12)
        eredmeny = "Dobott eredmény: {}".format(dice1)
    elif size == 20:
        dice1 = random.randint(1, 20)
        eredmeny = "Dobott eredmény: {}".format(dice1)
    elif size == 100:
        dice1 = random.randint(1, 10)
        dice2 = random.choice(dice100)
        sumdices = dice1 + dice2
        eredmeny = "Dobott eredmény: {}+{}={}".format(dice1, dice2, sumdices)
    return eredmeny