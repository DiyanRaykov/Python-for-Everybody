# Напишете програма на Python, която
# отговаря на низ, който има a,
# последвано от две до три 'b'.

import re
def text_match(text):
        patterns = 'ab{2,3}'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')
print(text_match("ab"))
print(text_match("aabbbbbc"))