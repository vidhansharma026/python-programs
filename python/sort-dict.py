# Creates a sorted dictionary (sorted by key)
from collections import OrderedDict
s = 'indiatry'
d={}
for i in s:
    c = s.count(i)
    d.setdefault(i,c)
print(d)
d1 = OrderedDict(sorted(d.items())) #items method is use to return key value pair
d1 = dict(d1)
print(d1)