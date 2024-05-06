#!/bin/python3

def is_leap(year):
    leap = ""

    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        leap = True
    else:
        leap = False
    return leap

year = 1992
print(is_leap(year))