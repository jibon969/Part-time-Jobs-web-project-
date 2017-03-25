
#******************* Python Numbers ****************

# Number data types store numeric values

# Numeric Types -- int, float, long, complex

# For example −

print('\nNumeric values in python : ')

a = 10  #int

b = 12.36  #float

c = 5192436 #Long

d  = 3.14j # complex

print(a,': int')

print(b,': float')

print(c,': long')

print(d,': complex\n')


#**********         Number Type Conversion     ***********************

'''

1.Type int(x) to convert x to a plain integer.

2.Type long(x) to convert x to a long integer.

3.Type float(x) to convert x to a floating-point number.

4.Type complex(x) to convert x to a complex number with real part x and imaginary part zero.

5.Type complex(x, y) to convert x and y to a complex number

with real part x and imaginary part y. x and y are numeric expressions

'''

print('Type Conversion :')

x = 10

print(x)

print(float(x)) # int to float

print(complex(x)) # int to complex

print('\n')


#****************** Mathematical Functions ***************

# The method abs() returns absolute value of x

print('Method abs() :')
x = 12
print(abs(x))

print('\n')


# ************* Number pow() Method ***********

print('pow() Method :')
x = 5
y = 6
z = x*y
print(z)

z = x**y # power
print(z)

print('\n')


#********   Mathematical Functions  *********************

# import math .. then all Mathematical Functions

print('Mathematical Functions : ')
import math # must declear import
print ("sin(3) : ",math.sin(3))
print('ten(90): ',math.tan(90))
print('Pi = ',math.pi)
print('degrees = ',math.degrees(20))

















