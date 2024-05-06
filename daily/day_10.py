#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(439)
    nstr = "{0:b}".format(n) + "0"
    count = longest = 0
    for i in range(len(nstr)):
        if nstr[i] == str(1):
            count += 1
        else:
            if count > longest:
                longest = count
            count = 0
    print(longest)
