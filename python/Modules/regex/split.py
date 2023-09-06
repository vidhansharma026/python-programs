import re

sp = re.split(r'Vidhan', 'vidhanName : My Name is Vidhan Sharma', flags=re.IGNORECASE)
fa = re.findall(r'Vidhan', 'vidhanName : My Name is Vidhan Sharma', flags=re.IGNORECASE)
s = re.sub('\s', ',', 'Name : My Name is Vidhan Sharma')
print(sp)
print(fa)
print(s)
