#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    # Write your code here
    tallest = max(candles)
    count_tallest = 0
    for candle in candles:
        if candle == tallest:
            count_tallest += 1
    return count_tallest


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # candles_count = int(input().strip())
    # candles = list(map(int, input().rstrip().split()))
    candles = [4, 5, 5, 5, 6, 3, 2, 1]
    result = birthdayCakeCandles(candles)
    # fptr.write(str(result) + '\n')
    # fptr.close()
    print(result)
