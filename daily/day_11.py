#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':

    arr = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]

    hourglass = [[0, 0], [0, 1], [0, 2], [1, 1], [2, 0], [2, 1], [2, 2]]
    greatest_sum = 0
    for y_offset in range(len(arr) - 3):
        for x_offset in range(len(arr[0]) - 3):
            total = 0
            for pair in hourglass:
                x = pair[0] + x_offset
                y = pair[1] + y_offset
                val = arr[x][y]
                total += arr[x][y]
            print(f'Total: {total}')
            if total > greatest_sum:
                greatest_sum = total
    print(greatest_sum)
