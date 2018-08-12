'''
Exercise01 - Mathematical Functions.

Chung Yuan Christian University
written by Woody Lo (the teaching assistant of Python Course_Summer Camp.)
'''

"""
' + ' is addition (加法).
' - ' is subtraction (減法).
' * ' is multiplication (乘法).
' / ' is division (除法).
' // ' is integer division (整數除法).
' ** ' is exponent (指數).
' % ' is remainder (餘數).
"""

# Addition
print("1+5=", 1+5)   # Answer is: 6

# Subtraction
print("6-4=", 6-4)   # Answer is: 2

# Multiplication
print("3*5=", 3*5)   # Answer is: 15

# Division
print("1/5=", 1/5)   # Answer is: 0.2

# Integer Division
print("7//3=", 7//3) # Answer is: 2

# Exponent
print("2**5=", 2**5) # Answer is: 32

# Remainder
print("7%3=", 7%3)   # Answer is: 1

# Absolute Value
print( "abs(5.6-7.8)=", abs(5.6-7.8) )  # Answer is: 2.2

# Convert to 'Integer'
print( "int(5.63)=", int(5.63) )        # Answer is: 5

# Convert to 'float'
print( "float(1)=", float(1) )          # Answer is: 1.0

# Rounding
print( "round(5.63)=", round(5.63) )    # Answer is: 6

# round(x, n) = Round off to the Nth decimal place.
print( "round(3.1415926, 2)=", round(3.1415926, 2) )  # Answer is: 3.14

# Maximum
print( "max(3, 5)=", max(3, 5) )        # Answer is: 5

# Minimum
print( "min(3, 5)=", min(3, 5) )        # Answer is: 3

# Complex number
print( "complex(3, 4)=", complex(3, 4) )# Anwser is: 3 + 4j


import math

# pi
print( "math.pi=", math.pi )            # Answer is: 3.141592653589793

# e
print( "math.e=", math.e)               # Answer is: 2.718281828459045

# Golden ratio
print( "Golden ratio=", (1 + 5 ** 0.5) * 0.5 )  # Answer is: 1.618033988749895

# Ceiling(取頂值)
print( "math.ceil(4.5)=", math.ceil(4.5) )      # Answer is : 5

# floor(取底值)
print( "math.floor(4.5)=", math.floor(4.5) )    # Answer is : 4

# sqrt = square root(平方根/開根號)
print( "math.sqrt(2.0)=", math.sqrt(2.0) )      # Answer is : 1.4142135623730951

# logarithm (base is: e)
print( "math.log(math.e)=", math.log(math.e) )  # Answer is: 1.0

# logarithm (base is: 10)
print( "math.log10(1000)=", math.log10(1000) )  # Answer is: 3.0

# logarithm (base is: 2)
print( "math.log2(3)=", math.log2(3) )          # Anser is: 1.584962500721156

# exponent
print( "math.exp(1.0)=", math.exp(1.0) )        # Anser is: 2.718281828459045

# sine
print( "math.sin(math.pi/2.0)=", math.sin(math.pi/2.0) ) # Answer is: 1.0

# cosine 
print( "math.cos(math.pi/2.0)=", math.cos(math.pi/2.0) ) # Answer is: 6.123233995736766e-17

# tangent
print( "math.tan(math.pi/2.0)=", math.tan(math.pi/2.0) ) # Answer is: 1.633123935319537e+16

# arc tangent = inverse of the tangent function
print( "math.atan(1.0)*4=", math.atan(1.0)*4 )           # Answer is: 3.141592653589793

