import os

directory = "two/sec"
parent_dir = "D:/python/Modules/thread" # makedirs will also make dir if dir missing in our path like one is not here

path = os.path.join(parent_dir, directory)
os.makedirs(path)
print("directory '%s' created"% directory)
