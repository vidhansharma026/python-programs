a = 'My Name is Vidhan Sharma'

# store = a.capitalize() # 	Converts the first character to upper case and lowercase rest of them if we give 1 character number it will do nothing 

# store = a.casefold() # Converts string into lower case if we give 1 character number it will do nothing

# store = a.center(50, 'X')  #  Returns a centered string 1 arg for length and 2 arg for a or chr to fill space around

# store = a.count('a')	#  Returns the number of times a specified value occurs in a string 1 arg for value 2 arg for start 3 arg for end  

# store = a.encode(encoding="ascii", errors="backslashreplace")  #  encodes the string, using the specified encoding. If no encoding is specified, UTF-8 will be used.

# store = a.endswith("Sharma", 5, 50) # returns True if the string ends with the specified value, otherwise False. 1 arg for value 2 arg for start 3 arg for end  

# store = a.expandtabs(10) # sets the tab size to the specified number of whitespaces.Default tabsize is 8

# store = a.find("Vidhan")  # Searches the string for a specified value and returns the strating position of where it was found 1 arg for value 2 arg for start 3 arg for end 

# a = "My name is {fname}, I'm {age}"
# store = a.format(fname = "Vidhan", age = 23) # Formats specified values in a string

# store = a.index('Vidhan') # finds the first occurrence of the specified value. 1 arg for value 2 arg for start 3 arg for end. The index() method is almost the same as the find() method, the only difference is that the find() method returns -1 if the value is not found

# store = a.isalnum() # Returns True if all characters in the string are alphanumeric it return false if it have space or special charactor

# store = a.isalpha() # Returns True if all characters in the string are alpha it return false if it have space or special charactor also

# store = a.isascii() # returns True if all the characters are ascii characters

# a = "\u0030" #unicode for 0
# b = "\u0047" #unicode for G
# c = "0123"
# print(a.isdecimal())
# print(b.isdecimal())
# store = c.isdecimal() # Check if all the characters in a string are decimals (0-9):

# store = a.isdigit() # returns True if all the characters are digits, otherwise False.

# store = a.isidentifier() # returns True if the string is a valid identifier, otherwise False.

# store = a.islower() # returns True if all the characters are in lower case, otherwise False.

# store = a.isnumeric() # returns True if all the characters are numeric (0-9), otherwise False.

# store = a.isprintable() # returns True if all the characters are printable, otherwise False

# store  = a.istitle() # returns True if all words in a text start with a upper case letter, AND the rest of the word are lower case letters, otherwise False.

# store = a.isupper() # Returns True if all characters in the string are upper case

# myTuple = ("John", "Peter", "Vicky")
# x = "#".join(myTuple) # The join() method takes all items in an iterable and joins them into one string.
# print(x)

# store = a.ljust(50,"x") # will left align the string, using a specified character (space is default) as the fill character.

# store = a.lower() # will left align the string, using a specified character (space is default) as the fill character.

# txt = "     banana     "

# x = txt.lstrip()

# print("of all fruits", x, "is my favorite")  #removes any leading characters (space is the default leading character to remove)

# txt = "Hello Sam!"
# mytable = str.maketrans("S", "P")
# print(txt.translate(mytable))  # Returns a translation table to be used in translations

# txt = "I could eat bananas all day"

# x = txt.partition("bananas")

# print(x)  #searches for a specified string, and splits the string into a tuple containing three elements.

# txt = "one one was a race horse, two two was one too."

# x = txt.replace("one", "three", 2)

# print(x)  # replaces a specified phrase with another specified phrase.

# txt = "Hello, welcome to my world."

# x = txt.rfind("e", 5, 10)

# print(x)# finds the last occurrence of the specified value. -1 if the value is not found.

# txt = "Hello, welcome to my world."

# x = txt.rindex("e", 5, 10)

# print(x)# finds the last occurrence of the specified value. raises an exception if the value is not found. 

# txt = "banana"

# x = txt.rjust(20, "O")

# print(x) # will right align the string, using a specified character (space is default) as the fill character.

# txt = "I could eat bananas all day, bananas are my favorite fruit"

# x = txt.rpartition("bananas")

# print(x) # searches for the last occurrence of a specified string, and splits the string into a tuple containing three elements.

# txt = "apple, banana, cherry, mango"

# # setting the maxsplit parameter to 1, will return a list with 2 elements!
# x = txt.rsplit(", ", 1)

# print(x) # splits a string into a list, starting from the right.

# txt = "banana,,,,,ssqqqww....."

# x = txt.rstrip(",.qsw")

# print(x) # removes any trailing characters (characters at the end a string), space is the default trailing character to remove.

# txt = "apple#banana#cherry#orange"

# # setting the maxsplit parameter to 1, will return a list with 2 elements!
# x = txt.split("#", 1)

# print(x) # splits a string into a list.

# txt = "Thank you for the music\nWelcome to the jungle"

# x = txt.splitlines(True)

# print(x) #  splits a string into a list. The splitting is done at line breaks.

# txt = "Hello, welcome to my world."

# x = txt.startswith("wel", 7, 20)

# print(x) # returns True if the string starts with the specified value, otherwise False.

# txt = ",,,,,rrttgg.....banana....rrr"

# x = txt.strip(",.grt")

# print(x) # removes any leading, and trailing whitespaces.

# store = a.swapcase() # returns a string where all the upper case letters are lower case and vice versa.

# txt = "hello b2b2b2 and 3g3g3g"

# x = txt.title()

# print(x) # returns a string where the first character in every word is upper case. Like a header, or a title.

# returns a string where some specified characters are replaced with the character described in a dictionary, or in a mapping table.

# store = a.upper() # returns a string where all characters are in upper case.

# txt = "50"

# x = txt.zfill(10)

# print(x) #  adds zeros (0) at the beginning of the string, until it reaches the specified length.


# print(store)