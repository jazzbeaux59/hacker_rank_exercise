'''
Given an array, a, of size n distinct elements, sort the array in ascending order
using a Bubble Sort algorithm. Once sorted, print the following 3 lines:

1. Array is sorted in numSwaps swaps.
where  is the number of swaps that took place.
2. First Element: firstElement
where  is the first element in the sorted array.
3. Last Element: lastElement
where  is the last element in the sorted array.
'''

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    #n = int(input().strip())
    #a = list(map(int, input().rstrip().split()))
    a = [4,7,2,1]

    a_len = len(a)
    num_swaps = 0
    # Traverse through all array elements
    for i in range(a_len-1):
        for j in range(0, a_len-i-1):
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if a[j] > a[j + 1]:
                num_swaps += 1
                a[j], a[j + 1] = a[j + 1], a[j]

    print(f'Array is sorted in {num_swaps} swaps.')
    print(f'First Element: {a[0]}')
    print(f'Last Element: {a[-1]}')
