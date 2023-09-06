# it will give an error if file exists
data = "this file is file7 and mode is x"
# with open('file6.txt', mode='x') as f:
with open('file7.txt', mode='x') as f:
    f.write(data)