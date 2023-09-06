import os

try:
	# If the file does not exist,
	# then it would throw an IOError
	filename = 'file1.txt'
	f = open(filename, 'r')
	text = f.read()
	print(text)
	f.close()

# Control jumps directly to here if
# any of the above lines throws IOError.	
except os.error: # os.error
	print('Problem reading: ' + filename)

