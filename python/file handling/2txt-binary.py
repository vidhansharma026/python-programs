f = open('file2.txt',mode='w')
f.write('Hello\n')
f.write('This is Vidhan\n')
f.write('I am his code\n')
f.close()

f = open('file2.txt', mode='r')
data = f.read()
print(data)
f.close()

f = open('file2.txt', mode='rb')
data = f.read()
print(data)
f.close()