#Project Title: Circular Garden Calculator
#Dan Rey G. Lumiib
#8-Adelfa

#Get the math library
import math

#get the radius input of the user in meters
radius = float(input('Please enter the radius in meters: '))

#Calculate the area using the math.pi
area = math.pi * math.pow(radius, 2)

#Calculate the circumference using math.pi
circumference = 2 * math.pi * radius

#Calculate the square root using math.sqrt
square_root = math.sqrt(radius)

#Calculate the answer that is going to be rounded up to a whole number
rounded_up = math.ceil(area)

#Calculate the answer that is going to be rounded down to a whole number
rounded_down = math.floor(area)

#Print all of the answer
print(f"The area of the garden is: {area:.2f}")
print(f"The circumference of the garden is: {circumference:.2f}")
print(f"The square of the garden is: {square_root:.2f}")
print(f"The rounded up area is: {rounded_up:.2f}")
print(f"The rounded down area is: {rounded_down:.2f}")