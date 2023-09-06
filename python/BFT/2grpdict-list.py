# def grouping_dictionary(l):
#     result = {}
#     for k, v in l:
#          result.setdefault(k, []).append(v)
#     return result
# colors = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# print("Original list:")
# print(colors)
# print("\nGrouping a sequence of key-value pairs into a dictionary of lists:")
# print(grouping_dictionary(colors))




colors = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)] # given list
print("Original list:")
print(colors)
result = {} # empty dict
for k, v in colors:
    result.setdefault(k, []).append(v)

print("\nGrouping a sequence of key-value pairs into a dictionary of lists:")
print(result)

# a = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# b = defaultdict(list)
# for key, value in a:
#     b[key].append(value)
# c = dict(b)
# print(c)