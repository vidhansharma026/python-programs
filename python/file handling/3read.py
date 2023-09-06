# if we dont specify mode by default it will read mode
f = open('file2.txt')

print(f.read())
print(f.readable())
f.seek(0)
print(f.readline())
f.seek(0)
print(f.readlines())
print(f.seekable())
print(f.tell())
print(f.writable())
print(f.fileno())
print(f.isatty()) #returns True if the file stream is interactive, example: connected to a terminal device.
# print(f.truncate()) # resizes the file to the given number of bytes.
f.close()