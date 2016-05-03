#!/usr/bin/python

#Simple dice rolling game. When prompted, computer will return a random value between 1 and 6

import random

def rolldice():
    print(str(random.randrange(1,7)))
    return

while(True):
    cmd = (input("Do you want to roll a dice (Y/N): ")).lower()
    if cmd == "y":
        rolldice()
        continue
    elif cmd == "n":
        print("Thanks for playing!")
        break
    elif cmd == "roll away":
        for i in range(10):
            rolldice()
        continue
    else:
        print("Please input 'Y' or 'N'")
        continue
