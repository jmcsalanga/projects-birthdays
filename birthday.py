# print a birthday message to the console using different adjectives each time (number of adjectives entered by user)
# default adjective printed = 1
# (use optional args - separate them by "and sometimes")
# (random choice)
# if input is invalid, you have to return the prompt

import random


def create_candle_top():
    candle_top = []
    dots = "*"
    for row in range(1):
        candle_top = []
        for col in range(1):
            candle_top.append(dots + "     " + dots + "     " + dots)
    return candle_top


def create_candle_body():
    candle_body = []
    dots = "-"
    for row in range(2):
        candle_body = []
        for col in range(2):
            candle_body.append(dots*3 + "   " + dots*3 + "   " + dots*3)
    return candle_body


def create_cake_layer1():
    cake_layer_1 = []
    dots = "|"
    for row in range(4):
        cake_layer_1 = []
        for col in range(4):
            cake_layer_1.append(dots*15)
    return cake_layer_1


def create_cake_layer2():
    cake_layer_2 = []
    dots = "|"
    for row in range(5):
        cake_layer_2 = []
        for col in range(5):
            cake_layer_2.append(dots*19)
    return cake_layer_2


def create_cake():
    cake = []
    candle_top = create_candle_top()
    candle_body = create_candle_body()
    cake_layer1 = create_cake_layer1()
    cake_layer2 = create_cake_layer2()
    cake.append(candle_top)
    cake.append(candle_body)
    cake.append(cake_layer1)
    cake.append(cake_layer2)
    for pos, row in enumerate(cake):
        for piece in row:
            print("\n", "{:^30}".format(piece), end="  ")
    print("\n")


def print_adjectives(*args):
    adj_list = args[0]
    adj_string = " ".join(adj_list)
    adjlist = adj_string.split()
    return adjlist


def main():
    while True:
        birthday_ask = input("How great do you think you are? Enter a number between 1 to 10: ")
        try:
            birthday_ask = int(birthday_ask)
        except ValueError:
            print("Dad is not 27")
            continue
        if 0 < birthday_ask <= 10:
            break
        else:
            print("DAD IS MOKULS")
    adjectives = ["pogi", "attentive", "hilarious", "intelligent", "scintillating", "generous", "kind", "spicy",
                  "determined", "rich"]
    picked_adj = random.sample(adjectives, int(birthday_ask))
    adjective_list = print_adjectives(picked_adj)
    create_cake()
    print("Happy birthday, Dad - you are (very) old", *adjective_list, sep=" and sometimes ", end="! I love you :-)")


main()
