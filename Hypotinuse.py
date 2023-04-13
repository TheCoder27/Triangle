import time
import math

base = int(input("What is the base of the triangle: "))
hight = int(input("What is the height of the triangle: "))

def check():
    step1 = (base**2) + (hight**2)
    hypotinuse = math.sqrt(step1)
    print("The hypotinuse is - " + str(hypotinuse))

check()