import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    first_sum = 0
    second_sum = 0
    j = n - 1
    for i in range(n):
        first_sum = first_sum + arr[i][i]
        second_sum = second_sum + arr[i][j]
        j = j - 1
    if first_sum > second_sum:
        return first_sum - second_sum
    elif first_sum < second_sum:
        return second_sum - first_sum
    else:
        return 0



n = 4

arr =  [[1, 2, 3, 4],
        [1, 0, 3, 4],
        [1, 2, 3, 4],
        [1, 2, 3, 4]]

result = diagonalDifference(arr)

print result
