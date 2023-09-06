# it will give error if file doesnt exists
# f = open('file3.txt',mode='+r')
f = open('file4.txt',mode='+r')

f.write("this file is file4 and mode is +r")
f.seek(0)
print(f.read())

f.close()