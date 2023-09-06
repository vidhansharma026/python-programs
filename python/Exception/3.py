try:
    f = open('myfile.txt', mode='w+')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error:", err)
# except FileNotFoundError:
#     print('No such file or directory')
except Exception as e:
    print(e)
    print(type(e))