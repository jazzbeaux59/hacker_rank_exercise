import sys

phone_book = {}
entry = query_list = []

for enum, line in enumerate(sys.stdin):
    if enum == 0:
        book_len = int(line.rstrip())
    else:
        entry = line.rstrip().split(" ")
        if len(entry) == 2:
            phone_book[entry[0]] = entry[1]
        else:
            query_list.append(entry[0])

for q in query_list:
    if q in phone_book:
        print(q + "=" + phone_book[q])
    else:
        print("Not found")
