'''
Exercise03 - Compute Circle Area with Input.

Chung Yuan Christian University
written by Woody Lo (the teaching assistant of Python Course_Summer Camp.)
'''

# Assign the pi.
pi = 3.1415926
print("pi:", pi)                             # pi: 3.1415926.
# Assign a radius using input.
radius = eval(input("radius: "))             # Take the user input as interprets code.

# Compute the circle area.
circleArea = radius * radius * pi
print("The circle area is: %f" %circleArea)  # The circle area is: 1256.637040.


'''
eval() interprets a string as code. The reason why so many people have warned
you about using this is because a user can use this as an option to run code
on the computer. If you have eval(input()) and os imported, a person could 
type into input() os.system('rm -R *') which would delete all your files in
your home directory. (Assuming you have a unix system). Using eval() is a 
security hole. If you need to convert strings to other formats, try to use 
things that do that, like int().
'''