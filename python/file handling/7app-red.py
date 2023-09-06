with open('file6.txt', mode='+a') as f:
    f.write('\n this file is file6 and mode is +a \n')
    f.seek(0)
    print(f.read())