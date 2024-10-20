if __name__ == '__main__':
    # x = int(input())
    # y = int(input())
    # z = int(input())
    # n = int(input())
    x = 1
    y = 3
    z = 2
    n = 2

    arr1 = []
    arr2 = []
    for i in range(x + 1):
        for j in range(y + 1):
            for k in range(z + 1):
                arr1.append([i, j, k])
    for item in arr1:
        if sum(item) != n:
            arr2.append(item)

    print(arr2)