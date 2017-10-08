def long_repeat(line):
    """
        length the longest substring that consists of the same char
    """
    # your code here
    if not line:
        return 0

    # Tally as long as the last character repeats. When the row is broken, start again from zero.
    counts = []
    last = None
    for char in line:
        if char != last:
            counts.append(0)

        counts[-1] += 1
        last = char

    return max(counts)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "own 1"
    assert long_repeat('aa') == 2, "own 2"
    print('"Run" is good. How is "Check"?')
