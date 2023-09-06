l = [1,1,1,2,2,8,1,3,3,4,5,5,4,8]

d = {}

for i in l:
    if i in d:
        d[i].append(i)
    else:
        d[i] = [i]
print(d)

# for i in l:
#     d.setdefault(i, []).append(i)
# print(d)

# using fromkeys() methods 
# d=dict.fromkeys(l,None)

# keys = list(d.keys())

# for i in keys:
#     v = []
#     for j in l:
#         if i == j:
#             v.append(j)
#     d[i] = v
# print(d)

# using zip_longest methods 
# from itertools import zip_longest
# val = [None]
# res = dict(zip_longest(l,val))
# print(res)


# using for loop 
# d = {}

# for i in l:
#     d[i] = None
# print(d)

# keys = list(d.keys())

# for i in keys:
#     v = []
#     for j in l:
#         if i == j:
#             v.append(j)
#     d[i] = v
# print(d)