# Write a Python program to search for
# a literal string in a string and also
# find the location within the original
# string where the pattern occurs.

import re

pattern = 'fox'
text = 'The quick brown fox jumps over the lazy dog.'
match = re.search(pattern, text)
s = match.start()
e = match.end()
print(f'Found {match.re.pattern} in {match.string} from {s} to {e}')
