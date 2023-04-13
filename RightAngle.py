base = int(input("What is the base of the triangle: "))
height = int(input("What is the height of the triangle: "))
hypotenuse = int(input("What is the hypotenuse of the triangle: "))

def check():
    if((base**2) + (height**2) == hypotenuse**2):
        print("Your triangle is a right angle triangle")
    else:
        print("Your triangle is not a right angle triangle - Get Better")

check()