# Now Function

'''

Syntax

def Function_Name(parentheses/ Argument):

        Statement 1
        Statement 2
        return expression
        
# Called the function

Function_Name( )

    
'''




# Now Example Of Function

'''

def Function_Name(name):
    print('Hello', name) # here print is a function

Function_Name('Jayed')
Function_Name('Hossain')
Function_Name('Jibon')

# to be wish --------------------


'''


# Now write a program to add two number and there sum using function

'''

def sum (a, b):
    return (a + b) # here return given tbe answer

x = sum(4,5)
print(x)

# or

print(sum(4,5))

print(sum(14,5))

# to be wish  --------------------

'''


# Example of Function 1.1

'''

def student_Score(name, score):

    print(name,'Score',score,'Marks')

x =  student_Score('marks', 78)

print(x)


'''



# Defenine initilizetion function in python

'''

def Student_Score(name = ' Jibon', score = 70):

    print(name,' Score ',score,'Marks')

Student_Score()

Student_Score('Score', 78)

Student_Score('Jibon', 88)

Student_Score('Marks', 78)


'''


# Multiple Parameter Function in Python


def cgpa(name, *score):
    print(name,score)

cgpa('Jibon',55, 66, 77, 75, 80, 83)
