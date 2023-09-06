f = open('file5.txt', mode='w+')

f.write('this file no is 5 and mode is w+')
f.seek(0) # itsets the pointer at start
data = f.read()
print(data)

f.close()