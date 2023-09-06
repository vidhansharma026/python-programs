import re

# user = input('enter any line :- ')
user = "My name is vidhan sharma"

store = re.sub('[aeiouAEIOU]', '', user)
print(store)