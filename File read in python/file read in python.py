# Now file read python

# ' r ' Opens a file for reading only.

# ' rb '    Opens a file for reading only in binary format



#------------------------  Now read this flie Jibon.txt  ---------------------------

'''

file = open('Jibon.txt', 'r')
print('\n',file.read())

'''


#------------------------- Another way to declera file read   ------------------------------

with open('Jibon.txt', 'r') as rf:
    a = rf.read()
    print(a)
    print(rf.mode) # Mode works file which mode



#------------------- Example of 3:  any location to read the file --------------------

# Desktop has a file >>> we read this  file how ?

with open('C:\\Users\\Jibon\\Desktop\\Bookmark.txt', 'r') as rf:
    x = rf.read()
    print(x)


