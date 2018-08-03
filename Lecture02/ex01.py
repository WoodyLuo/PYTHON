'''
Exercise01 - Fahrenheit degree to Celsius degree.

Chung Yuan Christian University
written by Woody Lo (the teaching assistant of Python Course_Summer Camp.)
'''

# Variable initialization.
fahrenDegree = ""
celsiusDegree = 0.0

print('______________________________________________________________')
print("This program is Fahrenheit degree to Celsius degree Convertor.")
fahrenDegree = input("Please enter a Fahrenheit degree: ")  # For user input.
fahrenDegree = float(fahrenDegree)                          # Convert strint type to float type.
celsiusDegree = (5/9)*(fahrenDegree - 32)                   # Convert Fahrenheit degree to Celsius degree.
print("%.2f Fahrenheit degree is %.2f Celsius Degree." %(fahrenDegree, celsiusDegree)) # print it out.

