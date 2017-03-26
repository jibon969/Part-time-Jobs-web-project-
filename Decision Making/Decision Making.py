#--------------------  Python Decision Making ---------------- ( Jibon )

# Python programming language provides following types of decision making statements

'''

if expression:

   statement(s)

   '''

# Example of IF Statement

'''

a = 6

if a >=54:
    print(a)

if a<=5:
    print(a)

if a == 6:
    print(a)

'''

# Example of  IF Statement

'''

a = 100

if a:

   print("1 - Got a true expression value")

b = 0

if b:

   print("2 - Got a true expression value")

print("Good bye!")

'''

#--------------   Python IF...ELIF...ELSE Statements  -----------------

# An else statement can be combined with an if statement

# else statement contains the block of code

'''

#  The syntax of the if...else statement is −

if expression:
   statement(s)
else:
   statement(s)

'''

# For Example

'''

a = 10

b = 20

if a > b:
    print('A is getter then B')

else:
    print("B is getter then A")

'''

# ---------  elif Statement  --------------

'''
Syntax of elif Statement :

if expression1:
   statement(s)
elif expression2:
   statement(s)
elif expression3:
   statement(s)
else:
   statement(s)

'''

# elif Statement


'''

x = 10

y = 10

if x > y:
    print('X is smaller then Y')

elif x < y:
    print('y is bigger then X')

elif x != y:
    print('x != y')

elif x ==  y:
    print('X is equal to Y')

else:
    print('Good bye')

'''


#-----------  Nested  if else in python ---------------

'''

a = 100

b = 150

c = 20

if a > b:

    if a > c:
        print('A')

    else:
        print('C')

elif b > c:
    print('B is big')

else:
    print('C is big')

'''


# Now write a program to take three number from user and which number are big

# using nested if else

a = int(input('Enter a number : '))

b = int(input('Enter b number : '))

c = int(input('Enter c number : '))

if a > b:

    if a > c:
        print('A is bigger then B and C')

    else:
        print('C')

elif b > c:
    print('B is bigger then A and C ')

elif a == b == c:
    print('A = B = C')

else:
    print('C is bigger then A and B')

