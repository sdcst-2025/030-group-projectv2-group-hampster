"""circle - Finlay
triangle - Finlay
volume triangular prism - Finlay
compound interest w/ reacuring input - Finlay
loan with compound interest interest and reacurring payment - Last person
Best price calculator - Finlay
Escape velocity calculator - Finlay"""

"""Template: 
    import math
    import os
    import time
    val = False
    while val == False:
        print("-------------------------\nPlease make a selection\n-------------------------")
        try:
            choice = int(input('To solve for radius type "1" \nTo solve for circumference type "2"\nTo solve for area type "3"\n'))
            time.sleep(1)
            os.system('cls')
            if choice in range(1,4):
                val = True
            else: 
                print("You entered an invalid input")
        except:
            print("You entered an invalid input")
            time.sleep(1)
            os.system('cls')
            val = False
"""

def circle(R):
    import math
    import os
    import time
    val = False
    while val == False:
        print("-------------------------\nPlease make a selection\n-------------------------")
        try:
            choice = int(input('To solve for radius type "1"\nTo solve for circumference type "2"\nTo solve for area type "3"\n'))
            time.sleep(1)
            os.system('cls')
            if choice in range(1,4):
                val = True
            else: 
                print("You entered an invalid input")
        except:
            print("You entered an invalid input")
            time.sleep(1)
            os.system('cls')
            val = False
    if choice == 1:
        a = float(input("Please enter the area of the circle: "))
        r = (a / math.pi)**0.5
        r = round(r,R)
        print(f"The answer is {r}")
        return a
    elif choice == 2:
        r = float(input("Please enter the radius of the circle: "))
        C = 2*math.pi*r
        C = round(C,R)
        print(f"The answer is {C}")
        return C
    elif choice == 3:
        r = float(input("Enter radius of the circle"))
        A = math.pi*r**2
        A = round(A,R)
        print(f"The answer is {A}")
        return A
    

def triangle(R):
    import math
    import os
    import time
    val = False
    while val == False:
        print("-------------------------\nPlease make a selection\n-------------------------")
        try:
            choice = int(input('To solve for height type "1" \n To solve for base type "2" \nTo solve for area type "3"\n'))
            time.sleep(1)
            os.system('cls')
            if choice in range(1,4):
                val = True
            else: 
                print("You entered an invalid input")
        except:
            print("You entered an invalid input")
            time.sleep(1)
            os.system('cls')
            val = False
    if choice == 1:
        A = float(input("Please enter the area of the triangle: "))
        b = float(input("Please enter the base of the triangle: "))
        h = 2*A/b
        h = round(h,R)
        print(f"The answer is {h}")
        return h
    elif choice == 2:
        A = float(input("Please enter the area of the triangle: "))
        h = float(input("Please enter the height of the triangle: "))
        b = 2*A/h
        b= round(b,R)
        print(f"The answer is {b}")
        return b
    elif choice == 3:
        b = float(input("Please enter the base of the triangle: "))
        h = float(input("Please enter the height of the triangle: "))
        A = b*h/2
        A = round(A,R)
        print(f"The answer is {A}")
        return A
def triangularprism(R):
    import math
    import os
    import time
    val = False
    while val == False:
        print("-------------------------\nPlease make a selection\n-------------------------")
        try:
            choice = int(input('To solve for height type "1" \nTo solve for surface area type "2"\nTo solve for volume type "3"\n'))
            time.sleep(1)
            os.system('cls')
            if choice in range(1,4):
                val = True
            else: 
                print("You entered an invalid input")
        except:
            print("You entered an invalid input")
            time.sleep(1)
            os.system('cls')
            val = False 
        if choice == 1:
            a = float(input("Please enter the first base of the triangular prism: "))
            b = float(input("Please enter the second base of the triangular prism: "))
            c = float(input("Please enter the third base of the triangular prism: "))
            V = float(input("Please enter the volume of the triangular prism: "))
            A = (4*V)/(((a+b+c)*(b+c-a)*(c+a-b)*(a+b-c))**0.5)
            A = round(A,R)
            print(f"The answer is {A}")
        if choice == 2:
            a = float(input("Please enter the first base of the triangular prism: "))
            b = float(input("Please enter the second base of the triangular prism: "))
            c = float(input("Please enter the third base of the triangular prism: "))
            h = float(input("Please enter the height of the triangular prism: "))
            s = (a + b + c)/2
            ab = (s*(s-a)*(s-b)*(s-c))**0.5
            A = 2*ab + (a+b+c)*h
            A = round(A,R)
            print(f"The answer is {A}")
        if choice == 3: 
            a = float(input("Please enter the first base of the triangular prism: "))
            b = float(input("Please enter the second base of the triangular prism: "))
            c = float(input("Please enter the third base of the triangular prism: "))
            h = float(input("Please enter the height of the triangular prism: "))
            V = (h/4)
if  __name__ == "__main__":
    R = 2
    triangularprism(R) 