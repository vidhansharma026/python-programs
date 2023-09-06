import os 

file = "file.txt"
loc = "D:/python/Modules/thread" 

path = os.path.join(loc, file)

os.remove(path) # this method only remove files not folder