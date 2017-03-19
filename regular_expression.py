# Python Regular Expression

# re.search()  is used to find the first match for the pattern in the string.
# Syntax: re.search(pattern, string, flags[optional])

import re

s = "my number is 123"
match = re.search(r'\d\d\d', s)
print (match)
print (match.group())

s1 = "python tuts"
match = re.match(r'py', s1)
if match:
    print(match.group())