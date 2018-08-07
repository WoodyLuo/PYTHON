'''
Exercise01 - Fahrenheit degree to Celsius degree.

Chung Yuan Christian University
written by Woody Lo (the teaching assistant of Python Course_Summer Camp.)
'''
import math

# Variable initialization.
fahrenDegree = ""
celsiusDegree = 0.0
'''
冒號 (Colon, ” : ”)
分號 (Semicolon, “ ; ”)
連字號 (Hyphen, “ – “)
括弧_圓弧 (Parentheses, 小括弧 “ ( ) 
括弧_方括” (Square brackets “ [ ] ”)
斜線 (Slash “ / ”)
反斜線 (backlash “ \ ”)
井字符號  (Pound key / Hash key “ # ”)
Calculation priority is:
Small Sarentheses > Exponent > Multiplication &  Division > Plus & Minus 
'''

Ans = 8 - 2 * 3
print("8 - 2 * 3 = ", Ans) # Ans = 2
Ans = (1 + 2) * 3 - 4
print("(1 + 2) * 3 - 4 = ", Ans) # Ans = 5
Ans = (1 + 2)**2 / 5
print("(1 + 2)**2 / 5 = ", Ans) # Ans = 1.8

s = "1.1"           # Assign value 1.1 to variable 'x'.
print(s)            # Print the value of 'x'.
print(len(s))       # Print the length of 'x'.
print(id(s))        # Print the address of the object in memory as integer.
print (hex(id(s)))  # Print the address of the object in memory as lowercase hexadecimal.

x, y = 1.1, 2       # Simultaneous assignment
print("x=", x, "  y=", format(y, '3d'), end=';\n')
x, y = y, x         # Swap
print("x=", format(x, '3d'), "  y=", y, end=';\n')


'''
DATA TYPE OF PYTHON:
  bool: boolean
  float: float
  int: integer
  list: list
  str: string
'''
bol = True
lst = []
message = "Welcome to Python"
print("Value of 'bol':", bol, "  Type of 'bol':", type(bol))
print("Value of 'y':", y, "  Type of 'y':", type(y))
print("Value of 'x':", x, "  Type of 'x':", type(x))
print("Value of 'lst':", lst, "Type of 'lst':", type(lst))
print("Value of 'message':", message, "  Type of 'message':", type(message))

value = 5.666
print("int(value): ", int(value))                # Convert the data tpye from float to int (turncate).
print("math.floor(value): ", math.floor(value))  # Take floor / Round down.
print("round(value): ", round(value))            # Round off to the first decimal place.
print("round(value, 2): ", round(value, 2))      # Round off to the second decimal place.
print("math.ceil(value): ", math.ceil(value))    # Take ceiling / Round up.
print("value: ", value)                          # Print original data.
