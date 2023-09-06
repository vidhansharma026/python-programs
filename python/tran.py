s = 'indiatry'

l = len(s)
d = {}

for i in range(l):
    c = 1
    for j in range(i+1,l):
        if s[i] == s[j]:
            c += 1
    if s[i] not in d:
        d[s[i]] = c
print(d)
keys = list(d.keys())
print(keys)
keys.sort()
print(keys)

sort_dict = {i : d[i] for i in keys}

# for i in keys:
#     sort_dict = {i : d[i]}

print(sort_dict)