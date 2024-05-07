class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

    # Add your code here
    def computeDifference(self):
        if len(a) >= 2:
            res = [(a, b) for idx, a in enumerate(self.__elements) for b in self.__elements[idx + 1:]]
            for pair in res:
                pair_diff = abs(pair[0] - pair[1])
                if pair_diff > self.maximumDifference:
                    self.maximumDifference = pair_diff


_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
