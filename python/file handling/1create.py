f = open('file1.txt', mode='w')
f.write('this file is file1 and mode is w')
f.writelines(["\nSee you soon!", "Over and out."])
f.close()