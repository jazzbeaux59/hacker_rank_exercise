#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    min = sum(arr)
    max = 0
    for i in range(len(arr)):
        x = sum(arr) - arr[i]
        if x < min:
            min = x
        if x > max:
            max = x
    print(f'{min} {max}')


if __name__ == '__main__':

    #arr = list(map(int, input().rstrip().split()))
    arr = [1, 2, 3, 4, 5]

    miniMaxSum(arr)
