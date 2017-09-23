from operator import mul
from functools import reduce

def checkio(number):
    all_chars = list(str(number))
    all_digits = map(int, all_chars)
    positive_digits = filter(None, all_digits)
    return reduce(mul, positive_digits)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
