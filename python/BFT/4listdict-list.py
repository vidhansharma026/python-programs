# Python3 code to demonstrate
# to convert dictionary of list to
# list of dictionaries
# using list comprehension
 
# initializing dictionary
test_dict = {"Science" : [84,89,62,95], "Language" : [77,78,84,80]}
# l = len(test_dict[1])
 
# printing original dictionary
print ("The original dictionary is : " , test_dict)
 
# using list comprehension
# to convert dictionary of list to
# list of dictionaries
# l = len(next(iter(test_dict.values())))
l = len(test_dict.values())
print(l)
res = [{key : value[i] for key, value in test_dict.items()}
         for i in range(4)]
 
# printing result
print ("The converted list of dictionaries " , res)
