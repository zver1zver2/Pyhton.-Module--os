import os

# How to check exist the file or path or not.

file_or_path = 'c:\\data\\file1.txt'
file1 = 'c:\\data\\file1.txt'

#variant 1
'''
os.access(path, mode)
Use the real uid/gid to test for access to path.
Return True if access is allowed, False if not.

mode:
os.F_OK - to test the existence of path.
os.R_OK - to test the readability of path.
os.W_OK - to test the writability of path.
os.X_OK - to determine if path can be executed.
'''

if os.access(file_or_path, os.F_OK):
	print('File (dir) %s exist.' % file_or_path)
else:
	print('File (dir) %s does not exist.' % file_or_path)

if os.access(file1, os.R_OK):
    fo = open(file1)
    text = fo.read()
    print(text)

#variant 2
try:
	fo1 = open(file1)
	text = fo.read()
    print(text)
except IOError:
	print('File (dir) %s does not exist.' % file_or_path)