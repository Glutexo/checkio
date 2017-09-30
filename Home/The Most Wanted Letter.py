from operator import itemgetter

def checkio(text):
    # Count frequencies of letters in given text, case-insensitive.
    frequencies = {}
    for char in filter(lambda char: char.isalpha(), text.lower()):
        frequencies[char] = frequencies.get(char, 0) + 1

    # Sort the letters by frequency in descending order.
    by_frequency = sorted(frequencies.items(), key=itemgetter(1), reverse=True)

    # Pick only letters with the same frequency as the most frequent one.
    most_frequent = filter(lambda item: item[1] == by_frequency[0][1], by_frequency)

    # Sort those alphabetically, return the first letter.
    return sorted(most_frequent, key=itemgetter(0))[0][0]

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
