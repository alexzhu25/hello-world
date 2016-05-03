#!/usr/bin/python

import random

def randomnumber():
    return random.randrange(1, 101)


goal = randomnumber()

while(True):
    cmd = (input("Guess a number between 1 and 100: "))
    if not cmd.isdigit():
        print("Please input a number")
        continue
    cmd = int(cmd)
    if cmd < 1 or cmd > 100:
        print("The number must be between 1 and 100")
        continue
    elif cmd > goal:
        print("The number is too high")
        continue
    elif cmd < goal:
        print("The numer is too low")
        continue
    elif cmd == goal:
        print("Congratulations! You have guessed correctly!")
        break
    else:
        print("Unknown error! cmd = {}".format(str(cmd)))
