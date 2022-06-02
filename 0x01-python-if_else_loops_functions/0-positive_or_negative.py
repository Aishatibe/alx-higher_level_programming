#!/usr/bin/python3
import random
number = random.randint(-10, 10)
for i in number:
    if i>0:
        print(i " is positive")
    elif i==0:
        print(i " is zero")
    else:
        print(i " is negative")
