import time
import math

base = int(input("What is the base of the triangle: "))
height = int(input("What is the height of the triangle: "))

def check():
    step1 = (base**2) + (height**2)
    hypotinuse = math.sqrt(step1)
    print("The hypotenuse is - " + str(hypotinuse))

check()