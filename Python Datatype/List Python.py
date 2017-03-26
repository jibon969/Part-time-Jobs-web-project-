
#***********************  List in Python ********************

# Python knows a number of compound data types, used to group together other values

# list of comma-separated values (items) between square brackets

# Lists might contain items of different types

#  ***********************####################***************

# Now how many to declear list in python

'''

a = list ()
b = []
c = [1,2,3,4]

print(a)
print(b)
print(c)

# How to known which data type of a ,b ,c

print (type(a))
print (type(b))
print (type(c))

print('\n')

'''

#*****************  Example of list     *********************



list = [1, 2, 3,[5, 6, 9],'Jibon', 'python', 3.6, [69.69]]

print('Complete list : ',list)

print('First element of the list : ', list[0])

print('last element of the list  : ', list[-1])

print('Starting from 2nd till 3rd: ', list[1:3])

print('Starting from 6th element : ' ,list[6:])

print('Prints list two times     : ', list*2)

print('\n')



#****************      More Example of list index   *******************

'''

a = [12, 'python', 16.2, 4,['jibon', 6.9, 'A'], True, [1, 'B'], 9, '12']

print(a)
print(a.index(12))
print(a.index('python'))
print(a.index(4))

b = a[4].index('jibon')  # multile list a[4] here index of 4
print('Index of Jibon : ', b)

print('Index of     A : ', a[4].index('A'))

print('Index of     B : ', a[6].index('B'))

'''

#************ Updating Lists ************

# add to elements in a list with the append() method

'''

c = [1, 2, 3, 4, ['a' ,'b', 'c', 'd'], True]

c[1] = ['jibon', 12, 13] # add element

print(c)

print('Print 13 : ', c[1][2]) #print 13

print('Print 12 : ', c[1][1]) # print 12

print('print 16 : ', c[3]+c[1][1]) # print 16


'''

#*************    add List Elements   *************************

'''

b = [4, 5, [6.9, 'A', 'b'], 9, 'jibon' ,'python', 69]

b.append('jibon')

print('Add Jibon : ',b)

print('\n')

'''

#*************** Remove List Elements *****************

'''

b.remove('python')
print('Remove python : ',b)
print('\n')

# More example of remove

list = [2, 6, 4, 'jui',[ 2, 4, 5 ], 2, 4, 5, 2]

list.remove(5)
print('Remove 5 list : ',list)
print('\n')

# Nested list remove data

list[4] = list.remove(2)

print('Nested list remove 2 :',list)
print('\n')

'''

#*******************  Basic List Operations **************

'''

print('Basic List Operations : ')

c = [1, 2, 3,3,7]
print('Length of list : ', len(c))

x = 3 in [1, 2, 3]
print('3 in list      : ',x)

y = [1, 2, 3] + [4, 5, 6]
print('add two list   : ', y)
print('\n')

'''

#***********  Python List extend() Method ********************

# The method extend() appends the contents of seq to list

'''

print('Extend() Method :')
a = []
true = 'This is true'
c = [1,2,3,4,['a','b','c','d'],True,true]
a.extend(c)
print(a)

# More Example of method extend()

a = []
x =12
y = 'python 3'
a.extend([x,y])
print(a)

'''

#*********** Count of list *************

'''
print('Count in list :')
l = [4, 5 , 6, 5, 7, 5]
x = l.count(5)
print(x)

'''
