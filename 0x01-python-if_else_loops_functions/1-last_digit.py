#!/usr/bin/python3
import random
number = random.randint(-1000, 1000)
if number >= 0:
    last = number % 10
elif number < 0:
    last = (-1 * number) % 10
    last *= -1

if last > 5:
    print(f"Last digit of {number:d} is {last:d} and is greater than 5")
elif last == 0:
    print(f"Last digit of {number:d} is {last:d} and is 0")
elif (last < 6) and (last != 0):
    print(f"Last digit of {number:d} is {last:d} and is less than 6 and not 0")
