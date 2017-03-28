#----------------    Loop in Python   ------------- ( 28-03-2017 at 9.40 am )

#  Python programming language provides following types of loops

# For loop

# while loop

# nested loops

# ---------------   Loop Control Statements  ----------------

#  Loop control statements change execution from its normal sequence

# Python supports the following control statements

#  1.break statement   2.continue statement    3.pass statement

# yntax for loop:

'''

for iterating_var in sequence:
   statements(s)

'''

# ----------------- Example of for loop  ----------------------

#1. print 0 to 9 all number

'''
for i in range(10):
    print(i)
'''


# 2. Now write a program to print 5 to 10 all number

'''
for i in range(5 ,11):
    print(i, end=' ') # end= ' ' use print one line

'''

# 3. Print 0 to 11 this value 0 3 6 9

'''
for i in range(0 ,10 , 3):
    print(i, end=' ')

'''

#4. list and print index value print like : 0 = jibon

'''

a = ['Jibon', 'Python', 3.6, 'A', 69]

for i in range(len(a)):

    print(i, ' index value : ', a[i])

'''


#5. char 30 to 40

'''

for i in range(30,40):
    print(i, ' = ', chr(i))

'''

# 6. char 50 to 100

'''

for i in range(50,100):
    print(i, 'Char = ',  chr(i))

'''

# Now write a program to print 3 line 1 2 3 4 5
'''
for p in range(3):
    for i in range(5):
        print(i+1,end=' ')
    print()

'''

# Now write a program to print 4 line to print 1 to 20

'''

for i in range(1, 26):
        print(i, end='\t')
        if i%5 == 0:
            print( )
'''

# --------------  Print *  ------------------------

# Write a program to print * in three line in 5 star

'''

for line in range(3):
    for i in range(5):
        print('*',end=' ')
    print()

'''

# Write a program to print * in 5 line in 7 star

'''

for line in range(5):
    for i in range(7):
        print('*',end='  ')
    print()

'''

#------------------- Example of print * ----------------------
'''
*
**
***
****
*****
'''

# Code Here :

for line in range (5):
    i = 0
    for i in range(line):
        print('*',end=' ')
        i = i + 1
    print( )


#

# 1.problrm
'''
******
****
***
**
*
'''

# 2.problem :

'''
        *
       **
     ****
    *****
  *******


'''

#problem 3:

'''
1
2 3
4 5 1
2 3 4 5
1 2 3 4 5

'''
