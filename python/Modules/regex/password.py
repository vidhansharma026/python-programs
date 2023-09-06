import re

pat = '[A-Z][a-z]{2,6}[@!\”#$%&]{1,5}[0-9]{1,8}'
store = 'Vidhan@123'

v = re.match(pat, store)

print(v)