import re

def stripString(string, chars='\s'):
    pattern = re.compile("(^{}*|{}*$)".format(chars, chars))
    return pattern.sub('', string)

print(stripString("  abc  "))
assert(stripString("  abc  ") == "abc")
assert(stripString("  abc  ", '123') == "  abc  ")
assert(stripString('123abc123', '123') == 'abc')