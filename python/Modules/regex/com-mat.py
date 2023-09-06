import re

com = re.compile(r'Vidhan') # use of compile method is we can reuse this pattern again in diff method  
print(com)
mat1 = com.match('Name : My Name is Vidhan Sharma')
print(mat1)

mat2 = re.match(r'Vidhan','Vidhansharma is my name Regular expression engine allows you to specify optional characters using the character. It allows a character or character class Vidhan either to present once or else not to occur. Lets consider the example of a word with an alternative spelling color Vidhan or colour') # match method only match pattern at starting otherwise return none
print(mat2)

ser = re.search(r'Vidhan','Name : My Name is Sharma Regular expression engine allows you to specify optional characters using the character. It allows a character Vidhan or character class either to present once or else not to occur. Lets consider the example of a word with an alternative spelling color Vidhan or colour') # search method match pattern in whole str otherwise return none
print(ser)

string = 'geeks'
pattern = 'g...s'

fm1 = re.fullmatch(r'Vidhan', 'Name : My Name is Vidhan Sharma')
fm2 = re.fullmatch(r'Vidhan', 'Vidhan')
fm3 = re.fullmatch(r'V....n', 'Vidhan') # re.match() matches only at the beginning but re.fullmatch() tries to match at the end as well.
print(fm1)
print(fm2)
print(fm3)

# string to be match save in a dictionary.
listString = ["string stay", "stringers sit","string"]
# loop through the dictionary and check for match
pattern = "(s\w+)\W(s\w+)"

for string in listString:
    match = re.match(pattern, string)
    if match:
        # matched groups are printed as a separate list
        print(match.groups())
        # matched groups are each printed as a single string
        print(match.group())
        print("***************")
