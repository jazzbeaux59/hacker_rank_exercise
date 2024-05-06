'''
Task
Read in two integers, a and b, and print three lines.
The first line is the integer division a//b
The second line is the result of the modulo operator: a%b.
The third line prints the divmod of a and b.
'''

import sys

lines = []
for line in sys.stdin:
    lines.append(line)
int1 = int(lines[0])
int2 = int(lines[1])
print(int1 // int2)
print(int1 % int2)
print(divmod(int1, int2))
