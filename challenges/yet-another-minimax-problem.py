#!/bin/python3

####
# Note: none of the below solutions work for all test cases
####

import math
import os
import random
import re
import sys

#
# Complete the 'anotherMinimaxProblem' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def anotherMinimaxProblem(a):
    # Write your code here
    #
    # borrowed a solution from the site
    # it doesn't pass all test cases either
    #

    # from itertools import *
    from itertools import product
    if a[0] == a[-1]:
        print(0)
    else:
        k = 31
        while not (((a[0] ^ a[-1]) >> k) & 1):
            k -= 1
    # print(min(x ^ y for x, y in product([x for x in a if (x >> k) & 1], [x for x in a if not ((x >> k) & 1)])))
    return (min(x ^ y for x, y in product([x for x in a if (x >> k) & 1], [x for x in a if not ((x >> k) & 1)])))

    #
    # my failed solution
    #

    # from operator import xor
    # import itertools
    # from collections import OrderedDict
    # # remove duplicate values from list
    # res = list(OrderedDict.fromkeys(a))
    # min_score = sum(a)
    # # perms = list(itertools.permutations(a))
    # perm_iterator = itertools.permutations(a)
    # # for perm in perms:
    # # for debug
    # count = 0
    # for perm in perm_iterator:
    #     this_score = 0
    #     for i in range(len(perm) - 1):
    #         x = xor(perm[i], perm[i+1])
    #         if x > this_score:
    #             this_score = x
    #     if this_score < min_score:
    #         min_score = this_score
    #     count += 1
    #     print(f'interation {count}')
    # return min_score

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # n = int(input().strip())
    s = "12 8 9 11 14"
    # s = "123 67 201 164 64 247 215 179 114 184 99 111 52 46 163 224 237 228 79 54 201 204 36 66 54 184 101 250 105 226 85 250 215 101 190 254 188 193 109 105 151 91 179 194 172 250 230 49 129 75 222 6 97 95 120 51 220 40 22 205 69 255 30 143 51 33 119 86 0 45 15 166 77 168 87 35 124 121 197 25 53 109 81 246 225 180 248 202 50 98 61 206 153 239 163 218 207 183 52 236"
    # a = list(map(int, input().rstrip().split()))
    a = list(map(int, s.rstrip().split()))
    result = anotherMinimaxProblem(a)
    # fptr.write(str(result) + '\n')
    # fptr.close()
    print(result)