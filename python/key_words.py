import keyword

# Get the list of all Python keywords
all_keywords = keyword.kwlist   # kwlist is a attribute that gives list of keyword
print("All Python keywords:")
print(all_keywords)

# Check if a word is a Python keyword
word_to_check = input('enter a word :- ')

if keyword.iskeyword(word_to_check):
    print(f"'{word_to_check}' is a Python keyword.")
else:
    print(f"'{word_to_check}' is not a Python keyword.")