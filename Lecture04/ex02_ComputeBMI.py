'''
Exercise02 - ComputeBMI Functions.
Chung Yuan Christian University
written by Amy Zheng (the teaching assistant of Python Course_Summer Camp.)
'''

weight = eval(input("Enter weight in kg:"))
height = eval(input("Enter height in meter:"))
bmi = weight / (height * height)
print("Your bmi:", bmi)
if bmi < 18.5:
    print("Underweight")
elif 18.5 < bmi < 24.9:
    print("Normal")
elif 25.0 < bmi < 30:
    print("Overweight")
else:
    print("Obese")
input()
