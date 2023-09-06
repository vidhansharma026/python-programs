import os

directory = "thread"
parent_dir = "D:/python/Modules"

path = os.path.join(parent_dir, directory)

os.mkdir(path)
print("Directory '% s' created" % directory)