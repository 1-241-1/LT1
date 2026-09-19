## Problem Identification
The problem is that you will need to develop a Python program that will determine information about the garden based on
a radius entered by the user.

## Problem Decomposition
I will need to break the task down into each unit that will require a solution from the math library.
First: Get the radius from the user
Second: Calculate the area
Third: Calculate the circumference
Fourth: Calculate the square root
Fifth: Round the area up and down
Sixth: Display the results

## Pattern Recognition
The pattern is that it will need formulas form the math library and display it

## Data Representation
The calculated answer will be display by its own print

## Algorithm Development
START
    IMPORT math

    INPUT radius (as float)

    area = math.pi * math.pow(radius, 2)
    circumference = 2 * math.pi * radius
    square_root = math.sqrt(radius)

    rounded_up = math.ceil(area)
    rounded_down = math.floor(area)

    DISPLAY "The area of the garden is:", area (2 decimal places)
    DISPLAY "The circumference of the garden is:", circumference (2 decimal places)
    DISPLAY "The square of the garden is:", square_root (2 decimal places)
    DISPLAY "The rounded up area is:", rounded_up (2 decimal places)
    DISPLAY "The rounded down area is:", rounded_down (2 decimal places)
END

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
