#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function accepts following parameters:
#  1. DOUBLE meal_cost
#  2. INTEGER tip_percent
#  3. INTEGER tax_percent


def solve(meal_cost, tip_percent, tax_percent):
    print(f'Meal cost: {meal_cost}')
    tip = meal_cost * (tip_percent / 100)
    print(f'Tip: {tip}')
    tax = meal_cost * (tax_percent / 100)
    print(f'Tax: {tax}')
    ttl_cost = round(meal_cost + tip + tax)
    print(f'Total: {ttl_cost}')


if __name__ == '__main__':
    meal_cost = float(10.25)

    tip_percent = int(17)

    tax_percent = int(5)

    solve(meal_cost, tip_percent, tax_percent)
