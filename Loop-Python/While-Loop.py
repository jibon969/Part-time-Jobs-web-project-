# -----------  while loop in python (28- 03- 2017 at 12.25 pm ) ---------

# The syntax of a while loop in Python

"""
while expression:
   statement(s)

"""

# char 1 to 49
'''
i = 0
while i<=50:
    print(chr(i))
    i = i +1
'''

# now write a program to number to char

# Examlpe 35 = #

'''

i = 0
while i<=150:
    print(i,' = ',chr(i))
    i = i+ 1

'''

# Now write a program to print 1 to 15

'''

a = 1

for i in range(3):
    i = 0
    while i <= 4:
        print(a, end='  ')
        i = i + 1
        a = a + 1
    print()


'''

# Now write a program to print 1 1 1 1

'''
i = 0
while i <=4:
    print('1  ',end='')
    i = i + 1

'''

# Now write a program to 1 2 3 4 5 in three line

line = 1

while line <= 3:
    line = line + 1
    i = 0
    while i <= 4:
        print(1 + i, end='  ')
        i = i + 1
    print()



