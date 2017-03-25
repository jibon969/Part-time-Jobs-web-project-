#***********    Python Strings           ****************

''' Strings in Python are identified as a contiguous set of characters

    represented in the quotation marks. '''


#*************** Example of String  ***************

str = 'Hello Python'

print('string Value    : ', str)

print('First characters : ', str[0]) # print first characters

print('last characters  : ', str[-1]) # print last characters

print('After all        : ', str[5:]) #print only python

print('Output th        : ', str[8:10]) # print only th

print('All string       : ', str[: :]) # print Hello Python

print('Before 8 all     : ', str[:8]) # print 8 index value


#example in String

a = "python class 4."

b = "pycharm & pythonist BP01."

print('output only 4    : ' ,a[-2]) # print 4

print('\n')

print('Output pythonist BP01. class 4. :')

print( b[10:]+ a[6:])

print( b[10:25]+a[6:15]) # Same out put

print( b[10:], a[7:])

print('\n')


# 1. ********* Now String Methon in python ******************



# The method len() returns the number of elements in the list

print('Len Method:\n')

c = 'Jayed Hossain Jibon'

print ('length of C : ',len(c))

# Example of len method

list1 = [123, 'xyz', 'zara']

list2 = [456, 'abc' 'Jayed', ' Jibon', 'Python', 69]

print ("First list length  : ", len(list1) )

print ("Second list length : ", len(list2) )

print('\n')




# 2. ***********    String find() Method     ***************

# Find method use to index value of list

print('Find() Method : ')

c = ' JAyed Hossain , 12'

print('12 index :',c.find('12'))

print('H index  :',c.find('H'))

print('\n')


# 3.  ************      Index of string    ***************************

print('Index of string :')

d = 'Jayed Hossain Jibon'

print('Index of e : ',d.index('H'))

#or

e = d.index('H')
print('Index of e : ',e)

print('\n')



# 4. **********    Ends with n true or false **********

print('End with : ')

d = 'Jayed Hossain Jibon'
x = d.endswith('n')
print('Ends with n : ',x)


'''

Pratice python shell

help> str

Help on class str in module builtins:

********************* Best of Luck ***********

'''
