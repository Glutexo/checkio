from string import ascii_lowercase, ascii_uppercase, digits

def checkio(data):
    # If the password is shorter than 10 characters, it is invalid.
    if len(data) < 10:
        return False

    # The password must contain at least one character from these given categories.
    chars = set(data) # All characters used in the password.
    for map in [ascii_lowercase, ascii_uppercase, digits]:
        if not chars.intersection(map):
            # No character from this map is used in the password: Password is invalid.
            return False

    # The password did not break any rule, it is valid.
    return True

#Some hints
#Just check all conditions


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
