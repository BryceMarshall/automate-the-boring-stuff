import re

def checkPassword(password):
    lengthCheck = re.compile(r'.{8}')
    upperCheck = re.compile(r'[A-Z]')
    lowerCheck = re.compile(r'[a-z]')
    digitCheck = re.compile(r'[0-9]')
    return lengthCheck.search(password) and upperCheck.search(password) and lowerCheck.search(password) and digitCheck.search(password)


assert(not checkPassword("abcdefghijhgfhg"))
assert(not checkPassword("1234567"))
assert(not checkPassword("12345678"))
assert(not checkPassword("Bryce Marshall"))
assert(not checkPassword("bryce marshall1"))
assert(not checkPassword("Bryc3"))

assert(checkPassword("Bryce Marshall1"))
assert(checkPassword("Bm345678"))
