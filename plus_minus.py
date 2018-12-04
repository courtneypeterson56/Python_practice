import math
import os
import random
import re
import sys

def plusMinus(arr):
    n = len(arr)
    positive = 0
    negative = 0
    zero = 0
    for i in arr:
        if i > 0:
            positive = positive + 1
        elif i < 0:
            negative = negative + 1
        else:
            zero = zero + 1
    positive = float(positive) / n
    negative = float(negative) / n
    zero = float(zero) / n
    zero = round(zero, 6)
    negative = round(negative, 6)
    positive = round(positive, 6)
    positive = '{:.6f}'.format(positive)
    negative = '{:.6f}'.format(negative)
    zero = '{:.6f}'.format(zero)
    print positive
    print negative
    print zero


arr = [1, 2, 3, -1, -2, -3, 0, 0]

plusMinus(arr)
