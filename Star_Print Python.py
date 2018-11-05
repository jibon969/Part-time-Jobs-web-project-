# Class 7 Solve the problem

# Now write a program user print star from user wish. Example is given below

'''
    *
    **
    ***
    ****
    *****

'''
a = int(input('Enter a number : '))
for i in range(a+1):
    for j in range(i):
        print('*', end=' ')
    print()

 # Now write a program print star  from user wish. Example is given below
'''
*****
****
***
**
*
'''

# Code :
num = int(input('Enter a nubmer : '))
for i in range(num+1):
    for j in range(i-1, num-1):
        print('*', end=' ')
    print()



import math 
print(math.pi)
	
