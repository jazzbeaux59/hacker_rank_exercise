#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    from datetime import datetime
    time_object = datetime.strptime(s, '%I:%M:%S%p')
    time = time_object.strftime("%H:%M:%S")
    return time

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # s = input()
    s = '10:45:35PM'
    result = timeConversion(s)
    # fptr.write(result + '\n')
    # fptr.close()
    print(result)
