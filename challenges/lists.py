'''
Consider a list (list = []). You can perform the following commands:

1. insert i e: Insert integer e at position i.
2. print: Print the list.
3. remove e: Delete the first occurrence of integer .
4. append e: Insert integer e at the end of the list.
5. sort: Sort the list.
6. pop: Pop the last element from the list.
7. reverse: Reverse the list.
Initialize your list and read in the value of n followed by n lines of commands
where each command will be of the 7 types listed above.
Iterate through each command in order and perform the corresponding
operation on your list.
'''

import sys

if __name__ == '__main__':
    arr = []
    lines = []
    for line in sys.stdin:
        lines.append(line)

    n = int(lines[0])
    for i in range(n):
        cmd = lines[i + 1].split()
        if cmd[0] == "insert":
            arr.insert(int(cmd[1]), int(cmd[2]))
        elif cmd[0] == "print":
            print(arr)
        elif cmd[0] == "remove":
            arr.remove(int(cmd[1]))
        elif cmd[0] == "append":
            arr.append(int(cmd[1]))
        elif cmd[0] == "sort":
            arr.sort()
        elif cmd[0] == "pop":
            arr.pop(-1)
        elif cmd[0] == "reverse":
            arr.reverse()
        else:
            print("Command not found")
