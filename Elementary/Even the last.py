def checkio(array):
    """
        sums even-indexes elements and multiply at the last
    """
    array_len = len(array)

    if array_len == 0:
        result = 0
    else:
        last_index = array_len - 1

        sum = 0
        for i in range(array_len):
            if i % 2 == 0:
               sum += array[i]

        result = sum * array[last_index]

    return result

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "An empty array = 0"
