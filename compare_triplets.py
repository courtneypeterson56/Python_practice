import math
import os
import random
import re
import sys

def compareTriplets(a, b):
    alice = 0
    bob = 0
    scorelist = []
    for i in range(len(a)):
        if a[i] > b[i]:
            alice += 1
        elif a[i] < b[i]:
            bob += 1
    scorelist.append(alice)
    scorelist.append(bob)
    return scorelist

a = [2, 4, 5]

b = [1, 2, 1]

result = compareTriplets(a, b)

print result
