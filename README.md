## Problem Identification
The problem is that you will need to develop a Python program that will determine information about the garden based on
a radius entered by the user.

## Problem Decomposition
I will need to break the task down into each unit that will require a solution from the math library

## Pattern Recognition
The pattern is that it will need formulas form the math library and display it

## Data Representation
The calculated answer will be display by its own print

## Algorithm Development
/ Circular Garden Calculator /

// Get the radius input of the user in metres
radius = input("Please enter the radius in meters: ")
radius = float(radius) // convert to a floating‑point number

// Calculate the area using π r²
area = math.PI pow(radius, 2)

// Calculate the circumference using 2 π r
circumference = 2 math.PI radius

// Calculate the square root of the radius
square_root = sqrt(radius)

// Round the area up to the nearest whole number
rounded_up = ceil(area)

// Round the area down to the nearest whole number
rounded_down = floor(area)

// Output all of the results
print("The area of the garden is: " + format(area, ".2f"))
print("The circumference of the garden is: " + format(circumference, ".2f"))
print("The square root of the radius is: " + format(square_root, ".2f"))
print("The rounded‑up area is: " + format(rounded_up, ".2f"))
print("The rounded‑down area is: " + format(rounded_down, ".2f"))

# Project Title: Circular Garden Calculator

## Description
This program can calculate the area, circumference, square root, and it can round it up or down based on what you need.

## How to run 
To run this problem you will need to input the radius of your circle, then it will calculate every thing for you

## Input Needed
The input you need is the radius of the circle you want to calculate

## Sample Output
If you type 5, then program will display the area of the circle which is going to be 78.52 square meters.It will also 
display the circumference which is 31.42 meters, after that it will display the square root of the area which is 8.86 
meters, it will also gonna be displaying the answer rounded up and down which is 79 square meters for the round up and 
78 square meters for the round down

## Author/Section
Author: Dan Rey G. Lumiib
Section: 8-Adelfa
