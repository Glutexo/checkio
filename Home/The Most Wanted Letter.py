from collections import Counter
from operator import itemgetter

def checkio(text):
    # Count only letters, case does not matter.
    frequencies = Counter(filter(lambda char: char.isalpha(), text.lower()))

    # Pick only letters with the same frequency as the most frequent one.
    most_common_frequency = max(frequencies.values())
    most_common_items = filter(lambda item: item[1] == most_common_frequency, frequencies.items())
    most_common_letters = map(itemgetter(0), most_common_items)

    # Return the alphabetically first letter.
    return min(most_common_letters)

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
