if __name__ == '__main__':
    # n = int(input())
    # arr = map(int, input().split())

    # test data
    data = "2 3 6 6 5"
    arr = list(map(int, data.rstrip().split()))

    from collections import OrderedDict

    # n = int(input())
    # arr = list(map(int, input().split()))

    # remove dups from inarray
    arr2 = list(OrderedDict.fromkeys(arr))

    # sort the list
    arr2.sort()

    runnerup = arr2[-2]

    print(runnerup)
