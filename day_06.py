import sys

in_list = []

for enum, line in enumerate(sys.stdin):
    str_in = line.rstrip()
    if enum == 0:
        test_cases = int(str_in)
    else:
        in_list.append(line)

for line in in_list:
    array = [x for x in line.rstrip()]
    str_even = str_odd = ""
    for enum, l in enumerate(array):
        if (enum % 2) == 0:
            str_even = str_even + l
        else:
            str_odd = str_odd + l
    sys.stdout.write(f'{str_even} {str_odd}\n')