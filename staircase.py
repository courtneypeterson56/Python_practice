import math
import os
import random
import re
import sys

def staircase(n):
    j = 1
    while j < n+1:
        print ("#" * j).rjust(n, " ")
        j = j + 1


n = 6
staircase(n)
