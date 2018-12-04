import os
import sys


def simpleArraySum(ar):
    sum = 0
    for i in ar:
        sum = sum + i
    return sum

ar_count = 5
ar = [1, 2, 3, 4, 5, 7, 8]
simpleArraySum(ar)
