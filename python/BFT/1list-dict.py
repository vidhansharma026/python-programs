# Python3 code to demonstrate working of
# Convert List to List of dictionaries
# Using dictionary comprehension + loop

test_list = ["Gfg", 3, "is", 8] # given lists value

print("The original list : " , test_list) # printing original list

key_list = ["name", "id"] # given list key 
 
# loop to iterate through elements
# using dictionary comprehension
# for dictionary construction
l = len(test_list)
res = []
for i in range(0, l, 2):
    res.append({key_list[0]: test_list[i], key_list[1] : test_list[i + 1]})
 
# printing result
print("The constructed dictionary list : " , res)

# test_list = ["Gfg", 3, "is", 8] # given lists value

# list_key = ['name', 'id']
# l = len(test_list)
# res = []

# for i in range(0, l, 2):
#     res.append({list_key[0] : test_list[i], list_key[1]: test_list[i + 1]})

# print(res)