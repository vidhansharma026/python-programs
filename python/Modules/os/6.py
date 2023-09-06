import os 

# file = "sec"
file = "one/two"
# loc = "D:/python/Modules/os/thread/" 

loc = os.chdir("D:/python/Modules/os/thread")
# path = os.path.join(loc, file)
# print(path)

# os.rmdir(path) # this method only remove empty folder
os.removedirs(file) # this method removes parent dir with child