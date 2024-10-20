#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code here
    for i in range(n):
        out_str = ""
        for c1 in range(n-i-1):
            out_str = out_str + " "
        out_str = out_str + "#"
        for c2 in range(i):
            out_str = out_str + "#"
        print(out_str)

if __name__ == '__main__':
    #n = int(input().strip())
    n = 5
    staircase(n)
