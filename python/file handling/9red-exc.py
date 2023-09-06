data = 'this file is file8 and mode is +x'
with open('file8.txt', mode='+x') as f:
    f.write(data)
    f.seek(10)
    print(f.read())

# output:- is file8 and mode is +x