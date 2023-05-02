print("Only works with integers")
base = int(input("What is the base of the triangle: "))
height = int(input("What is the height of the triangle: "))

def findArea():
    area = (base * height)/2
    print("The area of the triangle is " + str(area))

findArea()