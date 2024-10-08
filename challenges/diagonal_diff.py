#!/bin/python3

import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonal_difference(arr):
    # Write your code here
    sum1 = sum2 = 0
    num_elements = len(arr[0])
    for enum, i in enumerate(range(num_elements)):
        sum1 += arr[i][enum]
        sum2 += arr[i][len(arr[i]) - enum - 1]
    abdiff = abs(sum1 - sum2)
    return abdiff


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    result = diagonal_difference(arr)
    #fptr.write(str(result) + '\n')
    sys.stdout.write(str(result) + '\n')
    #fptr.close()
