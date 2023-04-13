base = int(input("What is the base of the triangle: "))
hight = int(input("What is the height of the triangle: "))
hypotinuse = int(input("What is the hypotinuse of the triangle: "))

def check():
    if((base**2) + (hight**2) == hypotinuse**2):
        print("Your triangle is a right angle triangle")
    else:
        print("Your triangle is not a right angle triangle - Get Better")

check()