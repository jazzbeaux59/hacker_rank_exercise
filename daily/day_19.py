'''
Complete the implementation of Calculator class, which implements the AdvancedArithmetic interface.
The implementation for the divisorSum(n) method must return the sum of all divisors of n.
Example
The divisors of 25 are 1, 5, 25. Their sum is 31.
'''
class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError


class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        result = 0
        r_list = range(1, n+1)
        for i in reversed(r_list):
            if n % i == 0:
                result += i
        return result

n = 100
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)